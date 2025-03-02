import sys
import platform

def get_platform_specific_module():
    current_platform = platform.system()
    if current_platform == "Linux":
        from .linux import LinuxPlatform
        return LinuxPlatform()
    elif current_platform == "Windows":
        from .windows import WindowsPlatform
        return WindowsPlatform()
    else:
        raise NotImplementedError(f"Platform '{current_platform}' is not supported.")