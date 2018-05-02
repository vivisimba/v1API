# -*- coding: utf-8 -*-
'''
Created on 2018年4月19日

@author: Simba
'''


import time
import datetime

import unittest
import config.config as CONFIG
import http_requests.http_requests as HTTP_REQUEST
import util.common as COMMON


class CivilTestCase(unittest.TestCase):
    
    civilAddByRepoIdSource = {
    "address": "addrerrTestAddCivil",
    "name": "test add civil by repoID",
    "id_type": "Id",
    "id_no": "371324199901012345",
    "images": [
        {
            "bin": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wDFAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRQBAwQEBQQFCQUFCRQNCw0UFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFAIDBAQFBAUJBQUJFA0LDRQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU/8AAEQgBEADQAwEiAAIRAQMRAv/EAaIAAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKCxAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6AQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgsRAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/dAAQAAP/aAAwDAQACEQMRAD8Ai+O3wnsfHGjQaloHhOy/tHQrQzyrpw2TvaFQCdoIWTYSrcDI5PrXq/7JFnr0v7Lmq+Htaikt9R0W+e/00SOpd4SwmQnBPOd45rxHSfEmqfBzVdT0vTdZuTZ6fFpV9YNqbid4LaeNxNaykgb13Jx0ODXuHwj8f/2J+07beHHU22gaxoCJBZsNqrM6mbAJ4Pykr7cVhiHSvyxjZNKP3ompX9rXdV+Rxv8AwUAtri18L6d460Lyojregz+HLl/KEmyOcLIgH907hIuffir3h+8itfhrr1xEgZIfD9rEJF46WsYz+Pp7V6D+0H4Ifxj+zP4/8KoN+qaA80lsR9791++jP/fO4fjXjN1qn2T9m3xReLh0lsba3T5sE/uIhjPrXThqnPSUnvbX1WjOpqNuVL+nscv8b3e0/Zq14PhCYPD9nEU6lhCJT+hr7f8Ah7axWHw48JW0EUcEKaRaERxKFUEwqScDuSetfCP7R7XI+CF7ZBx9ntdZsonA43+Vp0SL+TE8d6++PCsbQeEfD8TqVaPTLRSPQiFOK7KUkzzJK2j3Of8AjNpP9p/DXWp4pTBfabA19aSr1EijlfcMpKke4pPgtouqaF8M9Kt9Ztf7PvJWkufsTNlrZJG3Kh5ODyTjtuxXZtEk0e2WNJUJB2yKCOORwakkUyMCee5PvTdOPtVV62sYcl5KXYVRtXKkEHuajk+8MEetOklMajOMHoBVRptgyO/XitkytTP8XSCPwbr7Z5+wTc+nyGvl/wCE9lHa3NwEXy3fa5ye/evpPx1KR4I8Q4z/AMg+bhev3f5188/DKIjUGPBHAHtXJWS5kNJdD07x6Anhi4AxkQOeP92viv4hQbtOt5JG/dpLA+0EKC+1vmPqa+y/iVdLbeFL52yVFrIPzGK+N/HxB0uFcMT58eGHf5MkfhXFJr7R07xszlHWJYjcEjYqgu2OMfWuev8A4iaVYwKkCTS3T5CwhduMf3iePyzV7Vj51pIgVmCjkg4zXnWo2huLhljTzQvytgZx6c14k5xpy9xanlpKNRux6F8OvjVe+H/Fctx/Z8UFlc276ZdyLLuKJLgeYMgYZTg5BxgnNfReiXvhr4a/DGK41DxHYaHql5M0st1JKpuWUcJEiDLsu0bjgd6+UdHtY4oolEW90AJMjHLHHOcetV5rP7PevM8G2XIxnL/juPT0615laq5P2kvQwlXSleS1PTvGvxch8QpcJpVve61bO6zu8qm2juWX5VLOw3YA5woycdaz/AUZvPFf9r6miXFrZfvltAp8vgjCjJJIJwOc5rg77UJdP01zHKysDwoPUmo/Cfiy68N6PqcbK93dTzrJF55yiYHzFjnkZxhayqQhODa3/Ml+9FzW561rd9HcavrWs6xdW9tE8hlnuQQIol4AVM54AwABmsTwX48tvFPifV9G02MwaVfWHnWonOxpJbeTLPjsWRm79BXmGoPe+M9QZtavnkyrYS2jARGx/CnRfrU1pff2Dd211p9rFA1ngpFEMblH3lJ65YZ596MPSjSTlPWTCEPdcpbn0V4H8EazfwR6zHd6boegSO6/atdJEd1tOG8pEy7AdN2QM9Ca0dE0Lwlqvja/tp9GvNa1iG2+0aa9nO1u1w0XLpHGwILAfMBkEgHvXLXtpcahbQX7NcSWggj8gvysUWAVRV6KORwOM9a2J9Hkgi0XWo7gy+I7O4FwbeM/NCgOBuYYJJTdkDsa6YYicIcjWhVKXK1ocl8RPi5e6n4p+0WMSxW8MACx3SsrynHV/mb5vcHHHSunsLHw94j+Htn4jsIReXrXCQ6h5m7zY58cx4GMY4xjrnPNeY+N7aG48SXF3pcjS28sjYic4EYJzhfYdOa3vgXqEegeOb+51S/ttO0JdPa4vDdzLHEJUYLE4yfmfllGMnmtKdSNZ+zk9HovLzNY1FUlyP8A4Y77x+dS1W30TVdSW30/VvGfiKFZ7G3l86LT7CGEmG33nglQWZm7lj6V9e+DPFMtj+y/qXix9Oiuj4cg1C90lbyMMWihJMbI5yVBGQGB6DvX5peOvj3L4s0/wRoGheHL3QotL1SEf2rqLxzs27EePL27ScMTkk5r9W/jzqNpov7PHxAshJCsVp4XubcBI1jTiHb8qjhRnsK9qvzRlFLY9uEfeufP8H7Wuv3GsS6lf/BvXza+JdLjxa6Zq9lcmQovMgBZSMq2CCM186+Pvi1faf8ACKbwpD4N8Q6M9/rMaR3d9DC0Pk7h+5ARyS5UYHYnvXZfC7VH1j4GeEdUk8ybUNAnjt7mbBVpIhhDlx04KkZ6VgfG/SnbxZ4C05FEkN7r8Eg8v5xsi/eFj2zjvxXTF+znKEe9/v8A+CWm1Z9NvuOe+LHxOtPGvhXV9MTQNf0yV9cnvIm1Cz8uIAgIFdw5w+B93tjqa/VrTomTStOXylIFpAP/ACEtfkJqt2+reB7q5nkZvN8QyyqSBggyvjP4Gv2DtpY47W2TzACkESkE9MIornxspcsbhSSVxBEQcmBT7ikMWVH+j/rU4nQfx0olBA/eAfWvGdSS6s6rLsZ8sIbrZsQO/Fcl4912Pwl4X1LVZYGjW3QeWuQC8hIVVH1JFdxJIqDO4Y9a8E+OmoP4t8c+GvBlrIDbpMl1flW+6zHEYI9l3N+IqJVazcVGTu2gtFK7R0/xE3L8PPEoYkuNMkyRxztGf1r5/wDAt/Z+Hor3UdQnW2sLOIz3E7j7iKMkjHX2Fe/fFO4WH4d+J3Jwhs2TrgnJAxXyN4vuU1LwbfeHrG8ibUb4xKw+8EiVt7ZPQZwBzX2VafIlbojxUuZuxW+I37VF34z0u80/RdAXSbGYFI7+/l82Z4z38kABGI9Wb6V4bqGoXurSCW9vZ7jPzEF9qZAAHyjABwPSu0bwbY2bJHf3rXE3LAQfKc/TJ/nVWbRdEW48qysb/UJg3IJ/dg47tyc18zOOIxDvN2Q5RqzVjg5JpLPLR7QzqcLJxnnrXOajZ61dzw3bx28MAK/JFKFOM8grnPPrXr76PpunrHPrEQ02Jtv7mKbzH9gcDA/Oud1G6t5LSSOwuLW1BY4lAMhVPcjr+FKFCV9zGOFqJ3OYtrcwupZHADbgFzwPQnNW7d49TumsIsPdeUX2qTtCg+v40+x8J3OqP9n/ALTW5mdfMRIIGVgo6k5PT61oaj8OprC2t0ZY5FbMkRjkaK4U57HO0/jisY4Hln77ujm+qSveTOevrO7tYl06+tIEkGJ1mt5P9YASOc5P9Pasn7HIzEGMAHqc5x9PWum1fQNTtSt1dWjyiLannoAszKR0kAyGI9uauWfhW4uowxcFeCGABDCscTRamrLQjEKVNrl2OatNKZwcpINw4YgfrVLWLQWFtK9xKFGNiqzZbJ4HbpXqumeB7dADcu3IO+IE46dSe2K8f8feKbTVb64i0qNrzTYXWJG3gCUg/eHXIyODUxwk0ueexhTbqzUUe8/CPxVZad4P0rStRdP7FVVkEs23EMgHzN7Lnk16hf8AhqDT0nns79YRNbvKk0jB9ylegbHQg4H4V8j2V7F+4jvrZLy1UBBZsxVCT6leQB+ua9I8GfEh9OsW0CTT7ez064VY7WBS0rxnvtZmyq+3PtRNxltv2Oz3X6noPhvw/p1xFeTGzju4oVjMkE+ANpHJXHIIPUZriPi9o/hzw/JaRaRFcSajcRtNcW0hEsUCZG11fqGOfunoK6LU/EieGNIg0mwtidV1Jv313eXAht4lwcIGwcue3QVxPjLydd1N9U0mxaG1l2oxT94ryqoWQoVGMZGcDOM1lCKSu9P66GailHmZ4tcSNd3vhyUplpdRglzj7n79f6Yr9Vf2pdXWD9n/AOKG25DN/Y8yAbM5JZBwce9fk/dXL3M+iW8B8uf7dAkTuAArGUbSQeoz1r7k/aNvvjBp/wADfGg1rU/CN7orwRxXv9lKwutjSoPlBQDk4z+NfU11ZRuj6GEWlZM8+/Za1I6nqPivwgxjWDVtPEkMbSEsZFQK2FIweqn2xXS/EK0XUvB3h7xFujeXw/JLNNGCSVZIniYE9VOQOOleI/CXX5fCfxc8M6hDzGrzQTFgQPKZApz2zkgj6V9Q67oEWr/8Jp4elkJh1G3+1W7oNzssqYcKTjO1+3XPetZytKMuj0E4tJxXZM+aILjHwo0Yqd00+qxFlz0G7JI9ucf1r9VP+EmLiJ7S0uZ1KjdjYCuBzkF6/KK0ikl8B+FLBoZDe/bVJhCtlnyF8sjGeW446V9/rdeKo7rN98EmQoNpltZ2VsDoMKuPx61w4+cVypnRg1G8uZHq0fxC0mQ/vLswAHBMqMB/WtWbXLSLSf7Tk1C1h07Gftc06pF/30TjPt1rzex8ZrpiK8nwR1NSo5aMNI347oz3ryz42eO4/HPiDRJpNMvfD8OgxTo2mX0ymNZnK/vWQADcFBA3DjJrzKNONeXLFnXiZ0YRvTT+dj3a4+LvhCK1uJV8VaRceVE0nkRXa+ZJgZ2qD1J7CvnC/wDjnongnUp9Yv3/ALS8UX0huE0y2G6ZQSNoPZQBgZNfPPjr49tc31xp3h1TEYyVmv0UEFumF9B78/SvP7TWUtGyFYXErebPdSDLyN3LEnOa9KOXwhOM272POlOU4pNH0H4z+KGrePFm1fxReSadp5wYdOjnKxRc8Fv7x/DHtXIXXjbT4h+6u4p7Ujd9pkUxQljwqop+eQn/AHcV5P4n8XXmv3sWn2haX5B+9kJZd3oB3Pc9q6fw74a0vSbMX/ivxFFDcRAyJDEgeZjj0649yQPrXXOblrN2IXLDodNB9o120aW6mltkY4QyKFZvQhR09gc/SoY9M1O2mP2G+s7MY+e8v3Z3x0HyjAJ9jgVo6H4pivbPyNO0AusoMkd/fNmVl6Zwxwq+yjNJrOlz3Mdql7JHH8xZnU/KxA6DOKhO2jLTTTSMHVPA9jeRD7bdXHiTUOXa5MflqvOfkiBxx2ya0dB0m2stPaRULvkfO/zlR/dHb644qneTzW5I050kYNyXfcAPp3NU1vZ9NdZL+eeMlDhHGMkjqE/xp7rV6EPVaM6XSjHGLxjtWa5mySFAIUdF+lUNRuW1edzHMHEWEDdAMdcYx+lcbLqGrXKSW9vcGPzWH+mO4ATPXI9cVr6cGWdPMufNKoE8xmzn3qWnshu60aNPxPe32r6TNPYxRm2sZR5kbx4ZgOCVODyBzmrPhAszSRKfMguQskcjOGTPfB/+vS6PfRwWskOcyySsfk5UjHIOfaqunW6eHvEVzaWzyvCyrOil9wRj1CjsPaplGL0aMp0YTVzlfjb4r1DSNOOjWSXNnFPG327U40JKRnjy0A7kdTn2ry7wzpELtYwxESWSweeC33jyNoIHQ5zX0FqVzBqrzeczqWb54mH3W6cZFc6vw6tN1zeacTHdGIKVJBV8c4Az1rmqwcqdluciw6p07wOFvmjijWOWNN7nhg3II7Yrn7/UriO6jIlZGjYPFOG+ZCOmOPWunv0HnvHLH5cpO07lHDe3Fcxqtlm5k+8QvyhgT+leLCPsnqjzHJM27vxr4mv9Mc3V6Li1cc74I3ZPoQoYfUV6D8O/Glpb+DrXR5za6Z9umLfa2X7QjyjpvBAaGTGCCpwePpXnmhxq2iws0qxTq5RkfgEjr+GK7L4eeFdL8c+PNH8OarHNNaayJbUpCcvE/lsyyjPHy7emOQa6YTlKooy1LVROXIzx+5ZI/iJpNnEsawpqdo7HkY/eqWJzmvvb9rvxFBP8EPFMCappVwLq4tYwtnciR+bhcYHGRxzXnWgfshWEviOPWtQF4LlZUm+aTzEDgghgvGOldt+0J8KdT1T4bGPRLe98QX0upWhfTrS2BlMSvuZlHsQO4r6Fwm4xU1qj6rFypzrzlT0jfQ+X/CEYvPFcTn5RGXYYH3fmGOv+7X1tp2vDV7Dwnrj+Yq3O7Trh1YblLgkbx0wGXr7180+Hvhh8QvDeozz3vw08ZMkikALo0zKGJJ4KgjH0rr/DviLxX4W8C6roGo/D3xlJcT6g15aTjRpwsC5VlDAqCACG+6e9RWkvY8qd2tfnuZTd5p9DsvBvw8fUv2jfB+krERZwavLqzxk7tsUaCQgk/wC32PqK/Qu5nG55DCpZySeBnmvkH9m28vPHvi3WPEF14W1Tw/Lp1lHYxT39o0BnkmfdLtDj5gAg596+sTCLWxlvLt/LtLaIyT3EowkSKMszHoOBXlYmp7Wtyx2SRtSioRuc18SviFH4B8MSXUUEb6tc5gsICfvSEffIB+6g+Y/h61+aXxf8e3mv6tdaLa3Estirlry9zl7mUn5ssD0z19TXpv7T3xpuPHPiFrOwc2wni2RRKSGt7JgcLwMB5fvE9cYFfPF6LPQbR5JAdpx8vIG4jp15r1MFRdNcz3ZhOfM0U3P2OFYVVYwQMDGAo7sT1psUjIIzhwoHGBuLfzqKyilviLiUD97ltmOg7c8VJdzQaeqqOZHJ2nJwBiuqUW3qZKWtxjam2nzNFbKBKMliFBP0B6jHoKyoy01wJ7lnMjOGcSZbI+h4P0NWftZ808rlsMQB8oHTr60+YExkF1YpyQPur+PesGXvsbn/AAneqXdvG15NLGkb4SCN1LeWOACfT2rY0nxguqSNJfySSCNMW9uOQWJ4LHoAPbmvOVedkGEYxk4GeUP51Y0yaW2u1ea5aIBt20rkAf3fYVUYq3mSmloesQ395qFzHZ2rPb5GGmidRk+xPP8AWobvRLoSSfvZbmUrgyy3DE9evIH65rldI8XywXXmwCKMr0mMe5169M8D616DFr97Jo0bSX5F1MPkMRBYj346UaRQJpaM5nyptGkJkhkZ36AMTkjv0xUqXVzcSLLKhgiVeQzKST+ea6AeGxFZx3t3ullkZdqh/Xuc9hXO3Gk6c0ryS3OVTJYruZl9h0qOe6Gtdia18UWFnIMQC6uN5C5b5V9WPatnQvEkEuqvfm2WYqdiOSQjHHt2HWuQmtba7lcW0bLHngnliMdTxxWjosKW0riUs8m3auWJEX09zxRFWVhNOWp0djH/AGxHqzTvkxEEEHaOe+at+E53ltZogoFxC6jYpPz49D9McVl2mqyafdyvJHizCGMxlv8AW5H3mz/+urGkarFDLC8b/ZZGbKxocHGMfN/jUPyKsram54s8JR6pGl3ZWoOohdpiPHmce3evPtW8DS6jYRXcKxwybSJUccq6nBGT06GvWbPxAtzCkjMivCRGccj6/WuU+IjXFxMqaeAYbt/3r/dAJHPTpmuWagouTWljzcTQVueHzPOvA+mwT39/byuBAyBwjEZYjgkcc1qXHhuNJomyd0JLIElKsM8DBBBHHoe9X7DSINHkSUxjbGOgfnHfGa7fwp4v0bwfoeqa7cx/23C7pBHZLhV4bkMWB2kqe47cV50L1FaJ58VGUz9DI9IEpAEJyO6rVhfDcs7ALBI2B9xVzXm+m/Fjx7fyhT4Y1wDs134j061U+2IlYj8K6WfxB8Qr6xBTw3o1vIQNo1bxxcFfxEcQr6WeYYeHU9yOHqyeunqdtp3hnUrTBt4rqH2VTg/UdK3baTVLKMC4gg2k/wCsLLHn8zivnmy8I/FXU7oi81LwlDbBy6udZuL1QeyEboty+xrkPGH7L3xG8bx67A/jHw7ZR6mnlSPZ2MrNEpIJEO67Ii5HVQD+FcdStg6ybdjrp4StZWkvvR9bya1BPdxW7XOnvPgsIDcIz4HU4BPAr4B/ao+O2q3X7RXibw3LG0mk6JHDaW9lDcyJBKDGHZpEB2uSW7joAK+k/wBm79nbVvhBbXdtqF3p+pSXW3zb6OFIyowAVSJWYKTgEt1Jr59/bn+FXh/wD4qk8Xadf6hL4j8S3Qjl02URGAwpGFedGxvXHA64JzXDh/Ywre7s9F6mlWlKC5W035M+YdQ1OW+vtQ1q7cefcNtZiT9wdAPoAAK4MTp4m1CS5cEWls+yNGJPmH0GO341Z8Vas9xex6XasygL8z9NoHX8TUFhMkCYUYtIAEiRexxya+iTt6WOBWWprajqA0+yccCQ4JJOCT+uOK5eO5lklee4LneNoUvnOM8CrpAupo7ieR2VDuCPjDHtx3qtfTvOkcdupiQMCcAbsHtiqlGySI95bFO6ncSjZgTL1ODgKeg9zWkb9pLNcQs+QM56H3HrWXcjyJCoDEkfMVUnmrdhejiMyfu1Xhdh49sf1rgmujOlNLYsz28Vy2JC58v5isZ4FOjslSJWDLDbgkBy3yk9eTk81bdFuEUK6qDyCx5/DB4/Gs6XVrjTZ825jiJzlWwc+uTz+dTT2HFNO5pWDQWrhjPvLc4ibLAZ5PpW1b+IEinEyQ3F5dE7QZSSuMYBA28iuFfxNqszlQ6iIjgBFyP+BAZqDzJNVLMJ2WQAAmRzjHtWmiWom4roei/8J20ZlfULwLMoz5ap8yAdtuRzVOPxUdfkUWqtbWxDZeTA3H8O/tXDRW9vZsGmdJpWxvPJBOasXV0xMZXbuJAHAIVe3piqUUkmg1Oph1uKXVVjt3Z7e3y7uxIV+OnT6eta+oa8dLRHjJ3yIGcAfdyegyOT9KwvDGmLbTJ9qQpGzB3EXBl46E9hRq9yfFWpXDWTN9kgUxRM7MsYPck4OcfpUNRk9NkONo2uaR8beerbbYM5X5FkfOT7+1P0TT5NRuxfX+oN5rYXy1GOewx6dq5i/ittMkRLZFe4AA3lidxxyc1FY6jf2svnkKJ1bKySM0gT3GDgVDS6MSkpantFrfNpVk8EbnKtuZlGSSewFdHaK+r2V4suYQIQw2+uRzXgs3je4ubpUjnA+UBy+cKM8tx3x616p4I8Urq9v5McjOyIFEiAAMvcn3rN02obEuzumLqJWWxuLcyLHcK3yuMjNN0HwVLLo15qbSBYXQxEK2RLjGcjPbsTVXxFpr3+o38gaSO2tSu9iM7iRnavc4qT4U+KLHwp4t+yaxBFeeG9YZLK8hlBzbyMcRzoc8EHAOOx9q8J0+Wai3ZHheyUJuLP0D03S7lZ08yK5RRySUOBiunWQo21bl+gOGz/ACq0vwL8AqS0fhiGAnnFvd3UYz6jbKKreI/hB4YtPDmq3MKazZyW1lNLG1t4gv0wyxkg/wCux2rteVzTvGSPpvrcJb7jhMmcfaVI9c4pRcYP+uGP96pPDfwv0a28P6Uxu9flkls4ZHkk1+8ZmZowSTmTHU1pt8NdKYjy9Q16Eei6oz/q6sf1qHldXe6H7eC3M2HdcAbZVYHscHNfD/7c/ihD8QLOJZXebS9NEJiOQocsWI/UV91y/C6ElTB4q8S24HO3zbWTP4vbk1+bX7btgNI+OHiHSY7qW/FvbwI1zciMTSOwDFm2BVzjHRRwBXRhcFVoVY1JPYynWjJWifOkc7zySNIryySsQGLEkZ61eRzJKkWMAHblhz+FO0zTXurlLZFDOehVh8ufXvXpngX4O6hql+hkg/0aBOd4JLE9OelerOqoe83YiNO9ji00oLEA4bk8BiR+lR3MENrGvlQHzWG0vycAV2Gq6PG95dKsLhYJPKG37pYdT7471x/iMnzZLWIYaL5S/oT1H4e9OM7x5mXKmo6nLXsjQTyNuYsfvbckn6fnVe2keaUBwyAf89Bkn681buLOYSjYGYMeDtztPXrVu18L3N7OE2srnkBRk/jXI6qjJLoTGD6Is2csbGTY4DEA7gwwPw/xpzaZ9tkcRxFyxHCr1OK9W8J/BjUNQij862+barBePmz6mvWdC/Z+urloklKQxlcmONRx6ZP9K8+tmEKLtc9Ong5y12PlrRfhxq2s3LiCILEoPXJLY7dunrW9H8Hr6O2S5EbI6gD94uFx3wepya+6/D/wgtNJtVjlEKwgD90kfJPua6STw5p/keWtvGoA25IzivMqZtJ6QVjsjgIJan5s33gnVIZDGIipKn7o7fiBWMdKvIAwlRkjXjdJ2PYYFfoX4m8BpJZzKJcKQeIYk39O2RXg3i74LXevuotraQRxkKr3RGcDvgV0Us19pa+hlVwajrE+aQ8t6Taec/lkjd821Rj35/xrb1fxNb6fpjabZQxrKiJEJEkYCEAc7UHc9ct+VbfjH4eS+EgvmSLG7EqkSMFJ/wDrVwD2vksHlxK7cAA5Gc+te5TrQqwuePUg4WTKJaS8kjeQiQsDgnOR64q3p8jLlD5+BxgEAD6c0/UDEQPImM12cBihyiev41HbPLFJujDSbRkvIBgf41tZpXiYya6GothbQQmSS0Drlhy3JPrnNegeBPEZhgtkgiiww2u0fb0+tcfp1vNfiOA5nLthtowAT6AV1Fpp0vhvUdN8mBPMZxlf75H5Y+tZS95ijFLTdnpN1LJqHgaWeZdkwcK6qB8vzYNeZaou3T7ohiGCN83OV4PPv616Lqd058I3V0q7RPcBCqkH5xyQMn2rj7HQ28Q+IbLSYlLPf3KJkdlLAvgcdFBrzsTS5lFNHl14XkfsEkoPcfhWR41m2eCfEZ/6htwOPeMj+tfA9n/wVH8UI4S7+GuhFiD/AKrVZkJx9VNaDf8ABSi98ZW3/CPTfDSC1bVytj59vrJkaLzWCltvl9s5619Gndqx2qLPv3T4/K0yxQ/w20S/ki1YUYApojEKJGOQiKnPsoFOzx1pyd2TdvUXOAM45r8sf217G4h/aI8Y3D73imeJxKqjC/u1wufQDpX6mgZYD+Vfm3+2Wn9r/tG+LrAQiRUsbQoVBzv2HI4rGUnHYuGjPHv2fdAbXPGSLNGlwoyCH/h9OnU19uWPhSCDRntoALcyLhnUc8j+dfMP7Imkpd+LdSkQgm0hG5FJ4z04/A19iW4SNd0jBEXueBXi46TnUtFHt4WFoO54Z4p+Ekej2DS6Zp5muACLeJEyzux5Zh04614rqXwA1iD5ntZ/PkYu8jRZZ2PUgA197xtbTxB1kWQgDG01Bc2cMwyYlDYxnFeZWxVSgvd3Z206NOW58R6D+z29tE0l/auZUO7DjCr9emeK73wZ8HBb3H2q6jU7jlIh90L/APX619DXPhu2u08tl+XqQDgGobjTFi2CNBhentXh1cZWqJpvc9GFCmkkkZmm6RbWojVIVUIuFArYtUMLhiijB7VAIgGX5Ce3FXRGQOoyfSvPStudVkloWJLlhHgYA9aqmULk/LubrmpRCxjACnp0HSoJ49inIzgUrSZNrIz7gB2PT8jiuc8UG8S0MenwCSVxjcRwtdI6hmwVHPXnpVO/l8oKo5z6elbw92zZDaPnXxh8NZZopdQ1S5FxcsDxngHtxjpXzf4z0hbO7MSsBuOTxnb7Y4r7Y8cWEl/ZypFhiwJweK+RfiTZXMOqMzlUzwUUfd/GvqMvqyqafgeLjIaX6nn0+npEimcgZ6bB0PYcGklFwpjAYruYYBAx+JNPmuY22hQrLt+8Ozehx9KRUWVUPG9SCM8/iK+lhdx94+fa1szqNK1OPRrKe5+RZV2wwqxwXcnHHrgc5rp9PuhqOqaaJmU+Wy/ffDEkemfU9xXnN7PChhMAGc5dsdWHf3PvXa/BfRLjxh8R9Os5YBdW9vm6kUglcqfl3f4VSppu5UpONrH1T4W8DRT6Imn3EKGwkUNJG6A5PrnFU/C/wftPCvxLGrwPI2nwWbGzCkgJOx2sD77c4+vavQbLTb+RjvlW3gVcBEXA9qjjvdh5yAOOtKrFNK5hCKm7s+MzoN2cMfDEAJAz5dzH/wDE1ueDNMNr4w0NW0WG0d7yJVkeWNgSXA+UAZzjPWuoa2dSclcDqD2qLQCJPiP4NjK5V9UhAJGcHcBmto9EiIyT0Z+qtyALiTpgHFRq2KdcndcSHodxpgO0VovMEh6Hcyj6Cvz6+PWntf8A7Tfji/ePMcRtYVbqMLF/Pmv0EjbMiY6kivij4rIJ/iV4tkCgs17tfPHIUDFcld2Ssa07N2OJ/Y78OvpPiX4miWNhi4txG/8ACQQzYH5itj4x+MtTtL9rK0WcxxdRAjOSfcCu6/Z50s2lt4pu5YyBc3kflk90EYGPzzXoGp21orO86xkuODtGePeuCVlNua2SPYpKU4KMT4+0r466po1yiyyT/Z1bBWRWjIP/AALk17P4J/aH0nWRbwXl0qyHjC4bJ/MVb8VeE7DVw7zW63HP8ahs/nXkutfCjSYrgyW0TWMpOQMdD+HSvLr1MPUTU7o9CnQrU7PofUdj4lsr+NTFIrBhng81LLdxzggDAA4Ir5h8I6jrXgy4RZpftVsSFBXJP4/SvYLTxa80EbJ80rAZUdK8OrQUX7ruj06UlNWe53luqBSBhj65Gac0iJjOB9TXF3/ig21o8rDaQOnevIPEvxO1k3DJaSMF54GRj9aypYd1HccpqCuz6Jk1e3tfvuCBnO3tWbc+KdNA4uFQH+8f85r5Fv8Axl4z1Bt0ayjc3zMVyGwOmcdP1qCy1vxhNMkUmn3hQklmi3Nj2AP+NemsvjbWRxyxNtkfW8XiXT5ST56qR3z1qW5lin2sDkEdRXzZZJr0kSv9jvldhuKyIRjHt2r0bwdr2oymKO6yq8KUb+hoqYPkWjEq3M7HaXtlFInIw3uc5r5v+Onw7mu4J7uwVsPkMigfN3/Cvp6S2Mke4tgnpmuV8Q6Wuo2kkMsYbg4DVyUasqEk0KpaSaZ+dF1C9hIUlxEFOCp4Oc9yelQjUGgYuNmGyp7YGeMmu1+N2nxaZ4zubZPkTBZkXILHNefR2cwjQJA7CUlVTBJY+wr7SjU9pBSZ85OFpcqLlvOkoDyPiMFmIPIP0NfZn7Ivhy58K+CLjWZ9KFxf6swljkuE2FIv4R0yeK8f+EP7PEWoazpOpeLyy6ckiubFZo43lPYZbqOnHWvuCPxBaaPp0VlpugyLHAgjUTOqhQBxwo5/rXVRqQqaQd2ZVaU6SvJPUoTS61qkLl2itrYKT5cKYJA9+tYqpGwzuGPQ8Voa1d67qel3EscSRxxRFmhtkwzjPYk5Jrk7O7mkt1M0UttIOGjl6qa3qK1rswgjxfRLKbTvD9rbTsBNGp3BWLqmWJCBjyQoIUH2q14NRZfi74KjYYLahDhh0H7xetdjdaHaOXJg6dlOKx/DNlHb/G34fwxRj59Th4HQYYGiMLWMoyXNqfpZck/aZeedx/nTFboOxpJmzPJ2G4/zpoO08AU2ilsTQgeYp9xXxJ4+mE3jrxG8jYMuoOAWOAM46/SvtiAbpEHqRXwV4o8U29r478TNd6Smu281zcW8tqJjbyKSQFeOUKSjqRwcEHJBzXNUV2kzWnoz1v4Oi3n8CLfo5ElzNcNGqc5jV9iE5PQ4J49ah1y+igvFW6ufLOM99v8A9aj4FwX1nJrOitFFa+HtOhto9PtgVkdHZS0paUAFySR1/ACuj8T+GbC+V/tUQkAByB6V5uJ5VLlke9hVpdM52zuLe+jDR3lk0ROBuuUUn8Cck+1YniKzR7V2uNMvIDhm85VVkfHowPf3rh/G3wS8LajJcT6a8dleMuJY5ow6tx6Hp+FeZ6X8E9R0nUDcJ4ha2hQELDaI8YHpnDjI/KvJlSoSbanb5HfCtVT0Wh6NeQmxkKTW9xalkDql1A0TFT0Iz1B9a6Lwn5V7BtEsasvRXdVP/wBeuQ8OaLfQRSW+rar9vZMG2njiO8L3jbJPHoa774e6NaT6ldrJALlAqt5bRB2DHp2rz61PlT5HdHTGV99y1r+ipJYMXZEyM8yCvMLPTIrq8kiX966ZZhApk2gcZJHQfWvavFOnabDY7YrNIJW4Ecluqkn8q801W+v9B897VnJVN32a0+QtgfdCjGa5qN1H3mW1pqWNI0TR1UR3GoWajPPmzxr+HJro4NN0tBut5rGbb3S5jY/zrxR/jvqPha3e51LwMWgiYBkZirkHvjyiP1OK1dM/ac8Oa+CD4K1SwKLlpVEEqhj/AMBQnrXasPVnrZtfIiVel8PU9jivLS3WNXMIDnbH8w5PoOa0oYbFGVkRTKCMkDoa8h0j4v2EplfTtIvrKGeMxSudO2B1brk7SOo69feuq0bXsGzIlJgkypM3BQj8eeK2UJpW7dzOTjLpoehGIyhWG4ADlc5rH1/ydL0+S4nkWKIdXc4FXbXVI3jQWzC+lcHasJ3KCP7zDgVQk8Kvqs7XmoOLjy2Jij/gQ+w9vU1zcvMrtWMXofCHxliE/wARdSuruORw21beORSqiI9HyeSTj3Fb/gfwfNZ29pdPp8V2j4k/ekq0XuvFbf7UNj5Xjez3Bj9riEeexIcAA9x17V1sjar4LstLt9LtowbeJS/2lGeM4AGwenP1r6CVa2Hgo9dPuPNo0267urlPxxoN4lxpd19ky1zb7opNxbBH1r6c8HeL4bPwnpQvdLn1DUBbqJHR1Vc47k5rzzw7rtv8UPDgWezSC8tWJmh4Kr6kV0Nt4xi0TToraB7O3giX70kasePc1zYCcp1bJWsd+Y8sMJGEt7jPilrvivWvD1zBoVgunRgK7xWKs9xIucEBvU9cY5rB8OR65Fosv/CSxww6k0wEESsrSpGBgmXYSoYnoAeMc46VleJ/jdamLyIL6XV51OBFbkbVP+0R6fnRoeuTarZR3TExySHG3tXvzpSc1Pm26HykZe7otBtymzPr3waxPCcZn/aF+HaEAKdQjOf4iM+3b61NeSasgIF5ZsAOS1kwP14lqD4YRXs37R3gBbu4tZ1+1gjyISmBycHLtk8e1elNWtY5Y2ctNz9GnfdIxHdjSBR6c1GRlz9e1OBwOnSsGbomhba6seCOa/PXUrX7X4m8Rzyhoom1O4IAGMLv659a/QUvhWOcDaT+lfnz4nvxYW+rSA5ZrmdxkHn5zXLUV7FwtfU+jPBV5oTpdPptrY2Wtp5cerCwkfZOQg8mV42GEkKdccN1rcv9QQwkgJgjnI61ifDtbfXvhlpGqW1nHJqsdrHJc3MMQ857cr/HjBdVYH5uduecVDqkxSPchyjLkFTxXk4qbm3c+hwiXKlsYHiBIbossqI2eBuWuCuLC1W4dRBG2D/ECa6q8L3Dksec/pVFLKOOVmK5J65Oa+bm3zHuQglqZ8Gj/ZQJJo5FQq2xrcjzAcZHB4+ua6jQdHuNT0ndFaxWmoS7XaS3la1V8DjPl4+v41BGBNCqY3EkbQPTPIr0TSrI2scBIzIQCxxwfbiumU5Qo2t8zHkU53fQ8j8Y6heabIbbVUlSawJliaOVp3dH4J8xgGIGOFOcVj6lYS6po0d3bzJdyocrPCT869cEkA59a734n20cOpWupyLuiGYpwfu7WxyR3wayfN+yxJGhAjA6YHT1rnvGVOLa1Q4xfPvoebW1zdyS7WEeQdpV1/nmuj0y9MG0/wBk2c0q/wATIOfXmtDUdCWV/PjUBycsAeDU2m2O0YKgkHPPasJVU1orHRydTWsbRdYjcC3jhyOUX09a0rDShoLRS6e/2V5JVEkot4ZHUEfw+YjhTnuBUWmubWRJUxlSDz0x3qfxLriSpHFZod5KscjknI4/OrpSlTknBmc4rkakbiWryXE7SzzXd1PjzridhlsDAGFAUfgBUeoOkEG0AAjsKniuYrK2QSZ80jLE+prm9b1RUD5IKkfePUV0Ocp6vVnLNKMfI+XPj/aNr3xa8JWMOHaa6jUKef4wTnHTAFfS+pRRXOsCbZJPFDCI/Jhj3jjv+VeNw6YNc+LEGpSomLFSIGb5sSMMA/gM/nXuug6WPD9gUWbzpJyXmuZHJLE9hXRiJNQpwX9XMsGoucps4q10CDw5d6nqaQQ2CzQSKIEAUykjg47V4RB4UnvZP9PuLu4yx/1sjMSM+3FfQHj+e3VPJiRTctgtIeoHpXF2embh85EgHQ9MV6+W0HTi5t7nn5riI1JqC6HOab4Ss7FQkUYRQABgCuv0mF7WJViVVC8gKBSyQCFQw5xwDnOansQWbcQdo6kd69q3Kjwk7rU52cYRhnPHU+lSfB1TcftLeClwQkUnmMRjHQ4NMmzsORk/hzVv4ExCX9pjwxkjKxs2Dx/A38q65ya0OaDsz75V8n8e1KGB9KjB4GevtSh8tjk4GayNbpIdKx+z3GAMiFzj/gJr8xfiZ4xsdLtbhbu5WPzHchWbJb5j0A619PftP/te2Pw4tLzwt4UMOp+LriJoy5YeTZgjBdz6+g6mvz6TRWvLganrd2bonO+aYHMhPO1AeAOe1aRw8qrUnoi4vqfdv7NPic6z8GvCeo2M9xbTWpmiinSQrKu1yOvXofxrstcvmlmeSRY13Z3CJQi+5wOAa8Q/Y98UWuq+ANasLGA20elamUWMZO1JEDDr9DXs9+8bkNgs3oOOK+Zxt6NaaR9LhbTitDmri/gikC7JmJGcJgjHrnNZVx4igVSIrRnYnaBLJnn/AHVHP510U9pZyuS0I3L/ABZrLk023sbqG6hgVpI33qHJI4/nXz8q6lKyWp70IJLVnTeC/Dl9eTx3GoIkSryIQoXA+grv4ZY1mkGMbVwABXlHhn4sPe3OoWmpWhsbq3AZZFbdFMh7g9QR3BrTPj2KNGl80BMdc1WIcuSzMYR5m3sdH4nsl1DTZ4ZUEiupBUgc5ryGw1K10u7k0nX5L6zaI/6NqNsizlV7ebCSC647oQw966ez+Ofg+7v/AOzrjxHpiXwbb5DXSCTPpjNUvH+gW3inUtLl06eJbrD5dO644+vNc8Jcm6LtGasnqaOl6Ne6kP8AiUXGneJ4sZH9lXGJwP8Aat5tko/AN9aW50u90y4K3el6jZOeq3NlLHk/itc1a+CdUtgBNbx3UY5BU5IP41tpPq+lWyx/aNTtYAoXbFdTKpHp8rVu3h5apWf4DaqR0un+BaYvbgeafKU8AP8AKfyqaylWQ+a+MQHKjH3ie+fasW4vzcMDJvkdR1lJZvxzzVq0meG0klPQ/dUisdFrEwlJ21L9/qpZTtbpzx1rktX1F5kLc59jVi91DILbNmeSawLyVjE2/ndx1PFdVBSm1Y4a9TQm+H2raXp0upSakozL9xhEzE/QgVvzeK1hUrYl2jYYHmAgVz1kDZ20USAhEGBnn8aGmkkJweAevrXvrL1KXNJnkrMHTj7OCsR3he9meWZvMdjyfSmxp5ceQMDpjFO8yQDBIyeOKWMsCCzbVr14JU46I8uU3J3erIWXeuMt9KnsUkJyD8gOMdKWUlioRgRx6c1bt3by448DaO4xVaysTucddJy4OMYrW/Z8h839ozQpCv3Ek59P3Tcms27XeG6kfyNJ8MvFln8O/itB4m1KOWaztI3CxQbTJKxjZQq5IHU98CupKVR+6jCNr3PvwSKsZdmCKoyzMcACvjz9qH9tKy0Jrvwf4Guo7rVMbLzVI2DR2v8AsjGdzZ7dq5T4r/tZeIvGrTWOmxt4d0U5QwROrzTf77kdPZa8Hl+Ic2mFbdLO2JXP+rBiOfXK9/c13U8E42lV08ilJXta5xmnrqGqTtc3ULCGSQy3N7cbvMuWPU8jnnvWH4y1+S/mKSZZIfupHjGOgGPpXQ+JvGJ1BWKxGAvnc80hc89ufevM9Sm8x2DOwZTwuO3rW2IfsoKzNKL55Xex9G/sI+MRZeP/ABL4ZllCjWLJLq2B4DSQ5yPrtJ49q+w7+UohJ5x6dq/LHwJ4wuPh7430fxLZMwutOuFn2LjEidHXr3Umv04svE1j4q0Gw1vTJBLYajAs8LA/wkdD6EHIP0r4XMYa866n0GCnZ8o+a7WKPcxG49AO9RQXcdzGw3AMOwrC8UXq2duZGLZCHG08njpXl1h8RtQ8PiS7u9GvLiyD5cQMDKg91I/ka+aoxj7Ru+p7jnKWljvNRt/NlmCl42GSSB1rl4tFuPEQks4HaX5sOAMBQOxP9Kn0j41eFPEkExgjvdqYEyTQlWUE4wa2NO8eeFtGAhsriNQ53OrnaR9c12YiU1ZOOptShzoxIfhCltcM8cGnWczEgzC3y/13GvU/h74WtvCNu7tcS395N9+5lOcDsFH8I9hVO08SaTqUW+G7gk4BwHBqRvEkVqdqFWGcYU5/H2rgVSpNWkyk1S0sd35yOewPqajmnJGA/H5VyceuxyKNsgPHT1FW49VLoDuOCOueK5nF3FzKSNGcRuVdkBb1IyawtVdmXapxgeuOauSXQ8vcAMgc81i3kxIPQDPJNdEI8zOOpJN2MmeInA5yeorjfiP43tPBdnZPcqHe4mESIw4OOSePauwublVDcgrjtXxx+0H4xPiP4hpaqxa106LaiucAt1YjkV9HgKPPUXZHj4qXLGyZ9U6H4q03xLZq9nMnm4+aNiQRx1960BH5fUcnoR3r4/8ABni9g6NDepbyLg7WJXPtxxXsvh/4rOJYobudLkD5VcnAJ9M19cqH8h4D919z1vcFHJ5PrVdrkBucgHvSaZrVhfRp5hWFmxgF9wP410EOmW0kassaupxypyDXLKLhuiU77HPIWYZ5wex6VraeAyDIG0AdKvRWChl/dAY6c1KkKjhlHPGDUb6GqXU+c9K1nV7Wy8vVNen1S9cZd5AFRD6Ko9PU1Rv9UZRueRmK55cjjPpiuV1LXxcy5QP93BOOPqOaypdX3LkKCeuCcj8K+vcoUV7hyKDs02aWq6qkjOUldmAx8x/zmuZvrx5ZAw+fGMgcYou7psDYChPzHfzj61k3d3PDGSrDcvUgYOa5XUbdzaEVFWHatdGWydeNwBwM9u1cRLcSPL0y3QgZyfbNbep3m+Ir9/PBU96zdIhF3qlnGGIDuCcseQOcZGPzrycVVubwS0SZu+EvDTXV5HNLEysT8pIDHPtX1j8APFL6Vay+H7iZhaSv5truUDynP3kz6E847V4/a6L9jmjfbwACQozmu28KERa1a7sAMw+UEjnPFfD1cRKq7vZn0tOjGEP1Pf8AVIzeSASAkDvjpXaeEvDemX2m4uIoijgbxtGX9zXMRIJoVH3nxyTW3pGo/YbdVyVPXAauJU4xqbHRCpaKRznjv9n3w1rMxudNQaZdN/y3tCFI+vrXG618Htfmmhj/ALR02/8ALIYyz6epeQDs5Df0r1a511Xf5WC59e9U4tZZZTtnKFv4SQa3daps2elTUJxTkrniup/B3xJfSRbINMtFAILRWjneD/wIYq3p/wAEfHUCG4bxs0EK8JYi0+QAezEkfga9ui1ecKoZwUPQ8cU5tWVEYli/HcdK5p4ipy2SV/QmpCmtEvxPMdIt9R0+YwXwBZMZeJCA3HJwa66C8WGJtzDBUdR2qLVbkzuTtGD6dqwdSupoghyAhBG05rzlzSd2c8mlqdC2rKAwDK2B0HFZl/qaxoQWw3pWE984AwoHXOKyLq+M7BQ/TPOa9KlSWljzq0yTxH4iFlpl3PuJjijYsRnj6Yr4d8YC9i165lum3LcSF435HBNfa2r+G7rUvCGp3yYW0twA2VzuzXzJ4l0IX0U1qcF15Q9f5V9HgVCN3Hc8jEOSs3secWdzKs6NEzI/ALcCvTPD2ptOsReTc2MFu1eWXNs+mXM0ExUFCPl747Gt/QdUNmEXDupwTvNe/RqrRJHDKN0me3afqBUHMz+WvJUnn6iu/wDDvia+sokkt74tHgfIc4zXh+kav5iFQcAdEC4PryK6nQdcKAeaSmCBla9CMuZWZij3jTPiYxASe3Y7f44mH8s1fl+JWg2X/IQv/wCzQSB512rCIH03gYH44rx55vtMKPFIQSMgocEmrVvqU5PlSMrRuuGVlzkeh4rN0KUtVoym+V6nkEl8GRTkNnIxjk+tVPPUjhgu3rgngVz2q6hcJdiW23SBfvwtxnPUir1nqUV0hdXYMpwUIwR/9at3UjLS43CSSLxBEbFSGI5yef61m3oWYYyNy8nGePerRnZ0IGFUENx6VXkYynDMCM4J55HpWbdyOXoclfBlbYSm4HB7mtb4eW/2vxZpsIJH7xiAAD26YpdTswyBujHnao5H59qwYdSk0S+tbxVbfDIHAJIzg9/TivKru8HFdjqpNRsz6rsrIIBFjcMYDN1apba1az1a2cDgtnAOMDNTeHr2HW9Phu7UboZo1dXBGMHrWnLbYK/JkqM5NfAu0J6M+mhJSjoeu6deqbOGQEcKD1rftpI7uASKCNwOT6V5zo2o4sUy25QMflWrYa49nJuVgYiPmQHOfzrZyTCzRsX5FohG3cM/xcflVS3uUmmO2Pb2wetRXGrLcxqwAZTzhhVNL633Hd8j+u2uOrOV7I7KU3bQ6a0AaMHkE9Aavx2TMg5ARh0x1rnbHW1t0EZYyDsM9at23idELEBWyMkE9KwUavUcpJmt9gVOSM54+b1rn9ZWKOUBgGxnGOcVBrHjeNFURv8AMRkBQa4681GbU5QZCegwB3rppYeUlY4JzVtCS+v1nneKADavBYZGar28AIAIUAepJzVi3tWATIIz/D0q2LYqwK/NkfhXo6QSijibb1Z0emQI3wv8TRuT5TISCv0x+lfIviC3FrqsLht3nw/eUYAA5r621C4/s/4danCRjzlPCcZ7mvlPxEkUl6rAg/JhgQBg+hrsy27qTfoc2LV6cRngn4P6b8WrrU7aee8ttQtyPKmgQsoU9MjpXFfEb4S6v8ItSWK9k+12b/cuNjR4OehB/pXpPwv+MOrfCLUdTm0bSNN1Zb5VWSLVIGl2lf7hDptyPetrx5+1J4e+Inhm70Txb8P30+6YZhuNLufNVW90kGQPoxr6BxqRalFaHmQad0eJ6XfhvKBYs5UZYd/frXT6feEn5nG1gSW6ZrzWC6SK6ZYfMMDOfLY8EL2B9K6jRr8zSIh3Ng4yQMV3RlzJakuNmd3Y6rJaMpWQunXqOa0JvFdzIuyMHJHV2P8AKuZguWkTMm0qeOeoq3CQRwy4HHXFdim0KVup5812biVDI2FXGMgEgeppstsshWWJth67waraZH9oUZbcR94Enp2rSjAdDyvA5B/oelccLSsatWGWl+QoSZNoXjcpyeKsvKWAypO88YIOKheDeo27wCeGDDg9cCh1dPkbvxn0P1FbaLTcycmQykyxnO4qW4BHUenNcvqEbLLGWBIIOCR1FdPOqwqxKnHtzn61z+sqgMJXJGSMDpj65rhk3K5pCaeh6/8As9+NVhm/sK8kAwC9uxOSfUele+PbB1BVhg9utfD9ldy2VxFc2x8m6jYMsik5BFfR/wAMPjNbeIIYdM1XbbagigLKGwk359DXzGPwspXqwXqe1ha8YpQkz1OynEEhj5HoG6H6VdN+AwXA3GqE4URrJGdy4HzHpTVBcEjG4988189Gb+E9Tn0L0lxhcA7Tj+HrVRriaPAWYcDO0gk0zzsHaTyOMt2pk8hQAY4/D/CtLtWRm27e6xkt9dxD5SCGPTJyPcCsx9avwCM7fc8VeeTKhsZOODjpVYqJJTgEnoRmuiEv5kYSV1e4lpcvNOoJeVuDvOcZrrLOyAjXePmHfPSsfTbaOMFcFSTuzgDFdFbYaL5unY5rRSuzBQs7luOAcE4454NEgyyjIX1OMZpglSKIAAAj07VzXi7xlBodoIlYPeTcIg/h9zVRXM7ImSdtC7408SxDR5LYMBDByWQ9yK+ePEl+jTPMhyCQuFYVs+IPEkt3D9nSVZlLb5JMnOfoMVwmsagBMFLDA4JUck/1r38uwzg3KXU87E1VKy6Igv41nVcoJTyctb+aAe5OCKwdXs2SUOoUYUfL5DRAcds5zWqy+eSxMTDGGZ0kX+XaorhY54SAIHYDdjzJMn/vrNey39xyRV1ocigeKYoyfIOcdCT/ACrU0+5FtNy7LzlQlULuBnfIU7l6sTj69KtWTG5IR8h05Xng/Ss6a1sXbq9jttLvS0AOdy46Y6VpRuzEA4APY1x+jXhify3Gxjnrzz7V09vN+7U5OSuSQcV6EJNq7Mm7bo4vTVWzTDYG5ckBc1ehCo2B2HqMn3ArGikklfYqsB/ebpj8KnggkhOCSzL0yeBn+dcsZxgtDTR6GwjlFL8lSCdoUnJ+maVpWWIMoLMw+4DyTVCGZlG1zj0AFTSSKI8Ajaxxx3rRy5veY7roQ3aguD912UDAXse/WqWpW3n2TIhChQCFYdMe9XY1E48w4OBxgYzUxZgAPugjGewqVFO9ib8uyOSUlAUAGR3anpcPG4cZXb0YcYNWLi3W3kdN27ackmTJOarF+7KwJPGRXG4pLU0Tsep+CvjDqmjRR216739sAMPI2GT8e/4169ovj+x1hA8E6EMcFH4ZfqK+VUmKIMDdn/axWtY6u0cuQzo3O0qcEe4OK8ytgKVX3o6M6oYqdJJbo+ubW8guyCrKz+pGcirxt1mAJBx6kZ5r5fsvHupWcW6K6KuVIBfHB966vTfjPqtqULxxzIF/j4Lj+lePPLq67M9GOMh1Pc2s4yQec+lQugQk7ePUdK8nh+OtyECyafGx/vK5wP50N8ZpXVwLUA88kbfyoWCruylEHiabWh65bvls4OQOmea0obuOEHfII/UntXgc3xf1FU/cqqn+8R19qy7/AOIOqXz7DOVVsgqDjPGfxrell9ZyuznqYqMdT2LxX8SrTRkMcGLi4Y7QEwVU+pryLUvEFzfXMlxNP5s7nJlwdqj+6Ae1Ysk8lw5aTDEjoMcn6Cq892gXCbcju2cD617NHCRpPVXZx1K0pbE91ftEpEaAyEcNnoPX/wCtWRPcO8pLiOXaPulwh+ozVe4uftEuzeoPAUMcZz39asQFI0yGckEZlEAI57ZfFemoNao5HHmeqJIbmOFYyjRqx5AF+x49cge1TpcsVdvtMuXHyqL0cnvjcMVELpVzieVQoPyoYhgcdBmohqUBUgXbbc9T5LEfhmktGKMWlZIx9VgdZJZM5RmyGYq/H/Aar6axEq5Veew7VrXtxaXttuWZCo/i2R5z35BrDtVVpjh0ZVIYdxWkYpbo0tdam/q2kMY1nhZcEDKEjrV7StR+0LiXYZFAUjpVu0kaWBcZ6AgKMVjapZfYLppLcEoWBC7Oc/nzW72utyOR3M1QrNyoUrxuZTkfpQszuxPLgD7zD5Sf606SNRtL7tuTtfrwBTTLKqgLkKB1HGM9gOaxastgumrstK0jL29mAxxTDO8geNH3PjJyeAO4+tRCVoxy3JYAhj1OOlXooRFGNihsj5nc1UZOWhUbjEKIhKHgHAA4OPSnEjYGOAD/AHhmoll8iQlmLBv4M9KsMMZVSikdSRmnF233JvYydXiESrOSqhsBnJ6ccdaxTcxjk3EJzx95ST+Rr1b4V6/p3hb4neFdU1iwtNW0Nb5Ir+0volmhaGT5GLIwIOMhs9sV+mKfBz4azq8C+DvBDw44MelBuMcEkrXFiG6cr23KSvqfjut1bpgi4jJ6EHFTi5hKkeaGJGQM9Qa/UnVfgz4G0a63w+FfC8YBypg04EA/QpisrxD8KPBXjSw8nV/Dum36Ywjx2GyVOMcSLhxj2Nc0ZX1sOVj81IbhoYt2RtAz8wBHtWlDqSgDmSPscrn8jivpbxj+woyu03hTxNJADki21m1faPYSxqcDtyp+teM+Kv2d/iP4QuSLrwrc6ghIAuNFIvEYeuV5H4gVpzKTsTdvc5lb6BgSZVIyCpY4wKlSZFU4CgHod4IJ/Gsi/sL7T1CX2nX1lKDjbcW0qEAH0K9KbbXAlBwlw79NscTkj04Aqmymb9tdebjPlgDgsSen0q39rjt7X75bHIZQFBz2z1q14V+HHjHxnMF0DwZ4i1aRSAGttNm2Z92IAx9TXsWi/sQfFfUYBc+J4tE+H2lqA0l54h1SJCF9o1JyfqRTcuXqD0Wp4Vd38ZRiWMSKNzndhQPUnIr2n4A/sl+M/jtdQ3z2994a8IZ3vrD2uZbpcfdt0bG7P948D3r2L4a+B/2XvgrOdS8S/EKx8feI7eQOsr2kk0MDgdI4Y90Z5HDEmvQfEH/BSL4c6SvlaL4Z1zxK6AqXunXT4eOyjlj+QHvTXPPSCFzW9463wr/wTV+FGlqlxqOneNNVm6ML3Vkt43+oTGBXp2hfsrfBrwnAEtfhr4TRlH+t1i7F5Ifc53c18p6h/wAFPZDGG034X6Ha5+4b6/muGHpkKoFc1ff8FMfibdyFdJ0HwvoaZ4MOlvKScdcu2P0q1hqttfzQ9kfeNj8KvhzYqRbeD/h7Cg6Kmk+Zj/xytBPh34HI2r4X8CY750HP/stfnDP/AMFD/jpdPuh8QRW7Z+5BpVqo9uCCRWZcft/fH95ZNnjGVcAcC0tUwe4A21ccJLuvvGnc/S67+Dvw5vI28zwV4EmJGCW8OgjHpkLXwt/wUB+AngbwZ4dtvEnhXw74e0a8FwiTHRmkgOD6wMoGPcGvNF/bv+PcYDv49uyp67Uttw/ApiuS+K/7X3xW+JnhC50TxNrkWt6XP1S6sbclR0yrIAVP4VX1aUfe5k/mNM8s027IUKz4A6bifyrQuJP3Kuckg4CkdRWDos3npkfeUDoeTWw8SG1+8Qq8jBNdsVFilax//9k="
        }
    ]
}
    
    def test_addCivilByRepoId(self):
        # 添加civil
        addCivilByRepoIdUrl = "http://%s:%s/api/repositories/%s/entities" % (CONFIG.DEEP_IP, CONFIG.DEEP_PORT, "25f9ce2a-9070-406b-8fa7-37d42da935c3")
        civilAddByRepoIdSource = self.civilAddByRepoIdSource
        
        resAddCivilByRepoIdObject = HTTP_REQUEST.post_request(addCivilByRepoIdUrl, civilAddByRepoIdSource)
        print resAddCivilByRepoIdObject
        civilIdStr = resAddCivilByRepoIdObject[0]["id"]

if __name__ == '__main__':
    unittest.main()