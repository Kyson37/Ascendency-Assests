import pyautogui
from pyautogui import keyDown, keyUp
import time
import win32gui
import win32com.client
import sys
import win32con
import random
import keyboard
import tkinter as tk

def find_runelite_window():
    def enum_handler(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_handler, windows)
    for hwnd in windows:
        if "RuneLite" in win32gui.GetWindowText(hwnd):
            return hwnd
    return None

def bring_runelite_to_front():
    hwnd = find_runelite_window()
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        return True
    return False

def move_runlite_to_top_left():
    hwnd = find_runelite_window()
    if hwnd:
        win32gui.MoveWindow(hwnd, 0, 0, 800, 600, True)
        return True
    return False

def click_compass():
    hwnd = find_runelite_window()
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        randomx= random.randint(563, 585)
        randomy = random.randint(35, 60)
        pyautogui.moveTo(randomx, randomy, duration=random.uniform(0.1, 0.3))
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.click()
        print(f"Clicked compass at ({randomx}, {randomy})")
        return True
    return False

def push_camera_to_above():
    duration = random.uniform(3, 5)
    keyDown('up')
    time.sleep(duration)
    keyUp('up')
    print(f"Camera pushed up for {duration:.2f} seconds.")

def focus_and_move_runelite():
    hwnd = find_runelite_window()
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.MoveWindow(hwnd, 0, 0, 600, 400, True)
        print("RuneLite window focused and moved to top left.")
        return True
    return False


def click_banker():
    randomx = random.randint(360, 410)
    randomy = random.randint(250, 300)
    pyautogui.moveTo(randomx, randomy, duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.1, 0.3))
    print(f"Clicked banker at ({randomx}, {randomy})")
    pyautogui.click()
    time.sleep(random.uniform(1.0, 2.0))  # Wait for bank interface to open
    
def click_logs(): #Must be top left of bank in main tab
    randomx = random.randint(90, 107)
    randomy = random.randint(117, 130)
    pyautogui.moveTo(randomx, randomy, duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.1, 0.3))
    print(f"Clicked logs at ({randomx}, {randomy})")
    pyautogui.click()
    time.sleep(random.uniform(0.3, 1.0))  # Wait for logs to be selected
    
def close_bank():
    keyDown('esc')
    time.sleep(random.uniform(0.3, 1.0))
    keyUp('esc')
    time.sleep(random.uniform(0.3, 1.0))  # Wait for bank to close

def click_knife():
    randomx = random.randint(582, 592)
    randomy = random.randint(240, 260)
    pyautogui.moveTo(randomx, randomy, duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.1, 0.3))
    print(f"Clicked knife at ({randomx}, {randomy})")
    pyautogui.click()
    time.sleep(random.uniform(0.3, 1.0))  # Wait for knife to be selected
    
def click_log():
    randomx = random.randint(620, 640)
    randomy = random.randint(248, 264)
    pyautogui.moveTo(randomx, randomy, duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.1, 0.3))
    print(f"Clicked log at ({randomx}, {randomy})")
    pyautogui.click()
    time.sleep(random.uniform(0.3, 1.0))  # Wait for log to be selected

focus_and_move_runelite()
click_compass()
push_camera_to_above()
click_banker()
click_logs()
close_bank()
click_knife()
click_log()
