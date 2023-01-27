#%%
from AppKit import NSScreen
import Quartz
import ctypes
import objc

#Declare the active_displays array
MAX_SCREENS = 8
active_displays = (ctypes.c_uint * MAX_SCREENS)()

# Load the Core Graphics framework as a dynamic library
core_graphics = ctypes.CDLL('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/CoreGraphics.framework/CoreGraphics')

#initialize the active_displays array
for i in range(MAX_SCREENS):
    active_displays[i] = 0

#create a pointer to the display_id variable
display_id = ctypes.c_uint(0)
display_id_ptr = ctypes.pointer(display_id)

#Call the CGBeginDisplayConfiguration() function to begin the display configuration process.
display_config = core_graphics.CGBeginDisplayConfigration(display_id_ptr)

#Check if the CGBeginDisplayConfigration() function succeeded
if display_config:
    #Change the configuration using the methods of the display_config object
    # using set_mode() to change the display mode
    display_config.set_mode(0, width=1024, height=768)

    # call the CGCompleteDisplayConfiguration() function to complete the display configuration process
    Quartz.CGCompleteDisplayConfiguration(display_config, 0)
#%%
active_displays_ptr = ctypes.pointer(active_displays)

#Declare the display_count variable
display_count = ctypes.c_int(0)

# initialize the display_count variable
display_count.value = 0

# Create a pointer to the display_count
display_count_ptr = ctypes.pointer(display_count)

print(display_count_ptr)
#%%

displays = Quartz.CGGetOnlineDisplayList(MAX_SCREENS, objc.NULL, objc.NULL)

print(f'display: {displays}')
#%%









def change_resolution(display, new_resolution):
    # Get the screen object for the specified display
    screen = NSScreen.screens()[display]

    # Get the available resolutions for the display
    available_resolutions = screen.availableModes()
    print(available_resolutions)
#%%
    # Check if the specified resolution is available for the display
    if new_resolution in available_resolutions:
        # Set the new screen resolution
        screen.setFrame_(NSRect(0, 0, new_resolution.width, new_resolution.height))
    else:
        print("The specified resolution is not available for this display.")

# Example usage: Change the resolution of the second display to 1920x1080
#change_resolution(1, NSScreen.Resolution(1920, 1080))
# %%
