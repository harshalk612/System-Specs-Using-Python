# Importing the Libraries
import subprocess
import os
import math


def get_apps():
    print("\nThe Programs are", '\n--------------------------------------')
    cmd_apps = 'wmic product get name'
    programs = subprocess.run(cmd_apps, capture_output=True, text=True).stdout
    print(programs[5:])


def get_internetSpeed():
    print('\n--- This will take a while for testing ---\n')
    speed = subprocess.run(
        'speedtest-cli', capture_output=True, text=True).stdout
    sep_lines = speed.split('\n')
    print('The Speeds are:')
    print('-------------------------------------')
    print(sep_lines[6])
    print(sep_lines[8])
    print()


def get_Resolution():
    resolution = subprocess.run(
        'wmic desktopmonitor get screenheight, screenwidth', capture_output=True, text=True).stdout
    sep_list1 = resolution.split()
    scr_height, scr_width = sep_list1[2], sep_list1[3]
    print('The Heigh, Width, and Resolution are:')
    print('-------------------------------------')
    print(f'The Screen Height is: {scr_height}')
    print(f'The Screen Width is: {scr_width}')
    print(f'Therefore The Screen Resolution is: {scr_width} x {scr_height}')
    print()


def get_CPUName():
    cpu_name = subprocess.run(
        'wmic cpu get name', capture_output=True, text=True).stdout
    cpu = cpu_name.split("\n")
    print('The CPU Name is:')
    print('-------------------------------------')
    print(cpu[2])
    print()


def get_CoresThreads():
    cores_threads = subprocess.run(
        'wmic cpu get NumberOfCores, ThreadCount', capture_output=True, text=True).stdout
    sep_list2 = cores_threads.split()
    no_cores, threads_count = sep_list2[2], sep_list2[3]
    print('\n The No of Cores and Thread Count are:')
    print('-------------------------------------')
    print(f'The No of Cores are: {no_cores}')
    print(f'The Threads Count is: {threads_count}')
    print()


def get_GPUName():
    gpus = subprocess.run('wmic path win32_videocontroller get caption',
                          capture_output=True, text=True).stdout
    sep_list3 = gpus.split("\n")
    integrated_gpu, discrete_gpu = sep_list3[2], sep_list3[4]
    print('\nThe GPUs are:')
    print('-------------------------------------')
    print(f'Integrated: {integrated_gpu}')
    print(f'Discrete: {discrete_gpu}')
    print()


def get_RamSize():
    ram_size = subprocess.run(
        'wmic computersystem get totalphysicalmemory', capture_output=True, text=True).stdout
    sep_list4 = ram_size.split('\n')
    ram_bytes = int(sep_list4[2])
    ram_gb = math.ceil(((ram_bytes/1024)/1024)/1024)
    print('\nThe Total RAM in GB is:')
    print('-------------------------------------')
    print(f'{ram_gb} GB ')
    print()

def get_ScreenSize():
    scr_heighdim_inch = 8.24
    scr_widthdim_inch = 13.79
    diag_screen_inch = math.sqrt(math.pow(scr_heighdim_inch,2) + math.pow(scr_widthdim_inch,2))
    print('\nThe Screen Size in INCh is:')
    print('-------------------------------------')
    print(f'{diag_screen_inch} Inch ')
    print()

def get_EthWifiAddress():
    addresses = subprocess.run('ipconfig /all', capture_output=True, text=True).stdout
    sep_list5 = addresses.split('\n')
    eth_address, wifi_address = sep_list5[13].split(':')[1],sep_list5[55].split(':')[1]
    print('\nThe Addresses are:')
    print('-------------------------------------')
    print(f'Ethernet MAC Address: {eth_address}')
    print(f'WIFI MAC Address: {wifi_address}')
    print()

def get_IPAddress():
    address = subprocess.run('ipconfig', capture_output=True, text=True).stdout
    sep_list6 = address.split('\n')
    IP_address = sep_list6[10].split(':')[1]
    print('\nThe IP Address is:')
    print('-------------------------------------')
    print(IP_address)
    print()

def get_WinVersion():
    os_name = subprocess.run('systeminfo', capture_output=True, text=True).stdout
    sep_list7 = os_name.split("\n")
    win_version = str(sep_list7[2].split(':')[1]).strip()
    print('\nThe Windows Version is:')
    print('-------------------------------------')
    print(win_version)
    print()
    


# Main Function that have all the choices
if __name__ == '__main__':

    os.system('cls')

    print('\n--- Here all are the Choices You Can Have ---')
    print('1. All Installed Softwares')
    print('2. Internet Speed')
    print('3. Screen Resolution')
    print('4. CPU Model')
    print('5. No of core and threads of CPU')
    print('6. GPU Model')
    print('7. RAM Size')
    print('8. Screen Size in INCH')
    print('9. Wifi/Ethernet MAC Address')
    print('10. Public IP Address')
    print('11. Windows Version')

    user_choice = int(
        input('\nEnter the Choice You want from Above (Type 0 if you want all):-- '))

    if user_choice == 1:
        get_apps()
    elif user_choice == 2:
        get_internetSpeed()
    elif user_choice == 3:
        get_Resolution()
    elif user_choice == 4:
        get_CPUName()
    elif user_choice == 5:
        get_CoresThreads()
    elif user_choice == 6:
        get_GPUName()
    elif user_choice == 7:
        get_RamSize()
    elif user_choice == 8:
        get_ScreenSize()
    elif user_choice == 9:
        get_EthWifiAddress()
    elif user_choice == 10:
        get_IPAddress()
    elif user_choice == 11:
        get_WinVersion()
    elif user_choice == 0:
        get_apps()
        get_internetSpeed()
        get_Resolution()
        get_CPUName()
        get_CoresThreads()
        get_GPUName()
        get_RamSize()
        get_ScreenSize()
        get_EthWifiAddress()
        get_IPAddress()
        get_WinVersion()
