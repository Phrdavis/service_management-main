from tkinter import *
from tkinter import messagebox
from pathlib import Path
from datetime import datetime
from playsound import playsound
from configparser import ConfigParser
from contextlib import contextmanager
from PIL import Image, ImageTk 
import tkinter as tk
import threading,socket, os, gtts
import pymysql.cursors, re, uuid, time, multiprocessing


