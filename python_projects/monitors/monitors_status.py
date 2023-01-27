from AppKit import NSScreen
import ctypes
import argparse



class Display:
    def __init__(self, screen) -> None:
        self.width = int(screen.frame().size.width)
        self.height = int(screen.frame().size.height)
        self.scale = screen.backingScaleFactor()
        self.is_main = False
        self.is_mirrored = None
        self.screen = screen
        self.device_description = screen.deviceDescription()
        self.core_graphics = ctypes.CDLL('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/CoreGraphics.framework/CoreGraphics')

        # Load the Core Graphics framework as a dynamic library
        # core_graphics = ctypes.CDLL('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/CoreGraphics.framework/CoreGraphics')

        # Use the Core Graphics framework to determine whether the screen is mirrored
        self.core_graphics.CGDisplayMirrorsDisplay.restype = ctypes.c_bool
        self.is_mirrored = self.core_graphics.CGDisplayMirrorsDisplay(screen.deviceDescription()['NSScreenNumber'])

        self.is_main = self.is_main_screen(screen)



    def is_main_screen(self, *args, **kwargs):
        screen = self.screen
        main_screen = NSScreen.mainScreen()
        print(f'screen: {screen}, main: {main_screen}')
        return main_screen == screen

    def get_device_description(self):
        # returns a device description dictionary. Some sample output (for my reference):
        # {
        #     NSDeviceBitsPerSample = 8;
        #     NSDeviceColorSpaceName = NSCalibratedRGBColorSpace;
        #     NSDeviceIsScreen = YES;
        #     NSDeviceResolution = "NSSize: {72, 72}";
        #     NSDeviceSize = "NSSize: {2560, 1440}";
        #     NSScreenNumber = 4;
        # }
        return self.device_description

    def get_current_display_mode(self, display_id):
        return self.core_graphics.CGDisplayCopyDisplayMode(display_id)

    def set_resolution(self, width, height):
        # Use the Core Graphics framework to set the display mode of the screen.
        # Specify the return type of the CGDisplayMode function as c_int
        # self.core_graphics.CGDisplaySetDisplayMode.restype = ctypes.c_int

        # # Get the display ID of the screen
        # display_id = self.screen.deviceDescription()['NSScreenNumber']
        # print(f'display_id: {display_id}')

        # # Get the current display mode of the screen
        # current_display_mode = self.get_current_display_mode(display_id)
        # print(f'current_display_mode: {current_display_mode}')

        # #Create a CGDisplay object for the screen
        # # display = self.core_graphics.CGDisplayCreate(display_id)
        # displays = self.core_graphics.CGGetActiveDisplayList()
        # print(f'displays: {displays}')

        # Create a new display mode object with the specified width and height

        num_displays = ctypes.c_uint32()
        print(f'num_displays: {num_displays}')

        # Get the list of active displays
        active_displays = self.core_graphics.CGGetActiveDisplayList(0, None, ctypes.byref(num_displays))

        # Get the display ID of the screen
        display_id = self.screen.deviceDescription()['NSScreenNumber']

        # Create a CGDisplay object for the screen
        display = None

        # Iterate over the list of active displays
        for i in range(num_displays.value):
            # Get the display ID of the current display
            current_display_id = active_displays[i]

            # Check if the current display ID matches the display ID of the screen
            if current_display_id == display_id:
                # Create a CGDisplay object for the screen
                display = core_graphics.CGDisplayCreate(display_id)
                break

        new_display_mode = self.core_graphics.CGDisplayModeCreate(display, width, height, 32)
        print(f'new_display_mode: {new_display_mode}')
        print(f'ctypes.c_void_p(): {ctypes.c_void_p()}')

        # Set the display mode of the screen to the new display mode.
        self.core_graphics.CGDisplaySetDisplayMode(display_id, new_display_mode)

        # Release the current display mode and teh new display mode objects.
        self.core_graphics.CGDisplayModeRelease(current_display_mode)
        self.core_graphics.CGDisplayModeRelease(new_display_mode)
#%%

class CGDisplayMode(ctypes.Strucutre):
     _fields_ = [
        ('width', ctypes.c_int),
        ('height', ctypes.c_int),
        ('refreshRate', ctypes.c_int),
        ('bitsPerPixel', ctypes.c_int),
        ('IOFlags', ctypes.c_uint32),
        ('reserved', ctypes.c_void_p),
    ]


def get_displays():
    displays = []
    for screen in NSScreen.screens():
        displays.append(Display(screen))
    return displays



def print_displays():
    displays = get_displays()
    print(f'\nCONNECTED DISPLAYS:\n---------------------------------------\n')
    for display in displays:
        print(f'Display: {display.width}x{display.height} (scale: {display.scale}) (main: {display.is_main}) (mirrored: {display.is_mirrored})')
    print(f'\n')

main_screen = NSScreen.mainScreen()

main_display = Display(main_screen)

def get_valid_display_modes():
    core_graphics = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")
    core_foundation = ctypes.CDLL('/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')


    num_displays = ctypes.c_uint32()
    print('num_displays before',num_displays)


    # Get the list of active displays
    core_graphics.CGGetActiveDisplayList(0, None, ctypes.byref(num_displays))

    print('num_displays ',num_displays)

    # Allocate an array to hold the display IDs of the active displays
    active_displays = (ctypes.c_uint32 * num_displays.value)()
    selected_display = ctypes.c_uint32(0)

    core_graphics.CGGetActiveDisplayList(ctypes.byref(selected_display), ctypes.byref(active_displays), ctypes.byref(num_displays))

    print('active_displays: ', active_displays)


    # Iterate over the active displays and print their display IDs
    for i in range(num_displays.value):
        display_id = active_displays[i]
        print("Display ID:", display_id)

        display_mode = core_graphics.CGDisplayCopyDisplayMode(display_id)

        # Get the width and height of the display mode
        width = display_mode.contents.width
        height = display_mode.contents.height

        # Get the refresh rate of the display mode
        refresh_rate = display_mode.contents.refreshRate

        # Print the resolution and refresh rate of the display
        print(f"Resolution: {width}x{height}")
        print(f"Refresh rate: {refresh_rate}")


# main_screen.setFrame_(NSRect(0,0,1920,1080))

# main_display.set_resolution(1024,768)
# %%

# Create a new ArgumentParser object
parser = argparse.ArgumentParser()

# Add the --displays argument to the parser
parser.add_argument("--displays", help="List the displays and their properties", action="store_true")

# Add the --displays argument to the parser
parser.add_argument("--modes", help="List the valid display modes", action="store_true")

# Parse the command line arguments
args = parser.parse_args()

# Check if the --displays option is present
if args.displays:
    # Run the get_displays function
    print_displays()

# check if the --modes option is present
if args.modes:
    get_valid_display_modes()
# %%
