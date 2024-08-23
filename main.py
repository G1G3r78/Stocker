import multiprocessing
import threading

import apimoex
from kivy.lang import Builder
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.uix.image import AsyncImage
from kivy.utils import get_color_from_hex
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

from kivymd_extensions.akivymd.uix.charts import AKBarChart, AKPieChart, AKLineChart

import requests

#from requests_html import HTMLSession

#import requests
#from bs4 import BeautifulSoup

#{"Lukoil: 7000, "SBER": 3000, "PMSB": 3100, "YDEX": 4000}

Window.maximize()

if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions(
        [Permission.INTERNET,
         Permission.READ_EXTERNAL_STORAGE,
         Permission.WRITE_EXTERNAL_STORAGE,
         Permission.ACCESS_NETWORK_STATE]
    )


#pmsb_: list[float] = [0]
"""heads = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0']"""

scks: tuple[float] = (308, 6600, 3900, 280)


class Graph1(MDBoxLayout):
    def __init__(self, stocks: list = [], animation: bool = False, **kwargs):
        super(Graph1, self).__init__(**kwargs)
        #self.stocks = stocks
        print(stocks, 'graph1')
        self.size_hint=.8, .4,
        self.pos_hint={"center_x": .5, "center_y": .5}
        if len(stocks) > 0 and not animation:
            sigma = AKBarChart(
                y_values=stocks,
                x_values=[x for x in range(len(stocks))],
                radius=(40,),
                bg_color=get_color_from_hex("00ff7b55")
            )
            self.add_widget(sigma)
        elif len(stocks) > 0 and animation:
            sigma = AKBarChart(
                y_values=stocks,
                x_values=[x for x in range(len(stocks))],
                radius=(40,),
                d=0,
                bg_color=get_color_from_hex("00ff7b55")
            )
            self.add_widget(sigma)
        else:
            self.add_widget(
                MDLabel(
                    text="no info"
                )
            )


class RoundedIcon(MDBoxLayout):
    def __init__(self, **kwargs):
        super(RoundedIcon, self).__init__(**kwargs)
        self.size_hint = (None, None)
        #self.size = (None, None)

        with self.canvas:
            self.bg_color = Color(1, 1, 1, 1)
            self.rectangle = RoundedRectangle(size=self.size, radius=[75])

        self.bind(pos=self.update_canvas, size=self.update_canvas)

        ic = AsyncImage(
            source="https://companieslogo.com/img/orig/SBER.ME-10de1f5f.png?t=1720244493.png",
            size_hint=(.7, .7),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.add_widget(ic)

    def update_canvas(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size


class RoundedIcon2(MDBoxLayout):
    def __init__(self, **kwargs):
        super(RoundedIcon2, self).__init__(**kwargs)
        self.size_hint = (None, None)
        #self.size = (None, None)

        with self.canvas:
            self.bg_color = Color(.93, .1, .23, 1)
            self.rectangle = RoundedRectangle(size=self.size, radius=[75])

        self.bind(pos=self.update_canvas, size=self.update_canvas)

        ic = AsyncImage(
            source="https://companieslogo.com/img/orig/LKOH.ME-a19566ad.png?t=1720244492.png",
            size_hint=(.6, .6),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.add_widget(ic)

    def update_canvas(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size


class RoundedIcon3(MDBoxLayout):
    def __init__(self, **kwargs):
        super(RoundedIcon3, self).__init__(**kwargs)
        self.size_hint = (None, None)
        #self.size = (None, None)

        with self.canvas:
            self.bg_color = Color(1, 1, 1, 1)
            self.rectangle = RoundedRectangle(size=self.size, radius=[75])

        self.bind(pos=self.update_canvas, size=self.update_canvas)

        ic = AsyncImage(
            source="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Yandex_icon.svg/2048px-Yandex_icon.svg.png",
            size_hint=(.7, .7),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.add_widget(ic)

    def update_canvas(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size


class RoundedIcon4(MDBoxLayout):
    def __init__(self, **kwargs):
        super(RoundedIcon4, self).__init__(**kwargs)
        self.size_hint = (None, None)
        #self.size = (None, None)

        with self.canvas.before:
            self.bg_color = Color(0, .4, .6, 1)
            self.rectangle = RoundedRectangle(size=self.size, radius=[75])

        self.bind(pos=self.update_canvas, size=self.update_canvas)

        ic = AsyncImage(
            source="pmsb.png",
            size_hint=(.7, .7),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.add_widget(ic)

    def update_canvas(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size


class RoundGraph(MDBoxLayout):
    def __init__(self, stocks: list = [0], **kwargs):
        super(RoundGraph, self).__init__(**kwargs)
        #self.stocks = stocks
        pmsb_zeroless = [cock for cock in stocks]
        pmsb_zeroless.remove(0)

        if len(stocks) > 0:
            total: float = round(sum(stocks), 2)
            #print('total -', total)
            percs: list[int] = []
            for i in range(len(pmsb_zeroless)):
                p: int = round(pmsb_zeroless[i] * 100 / total)
                percs.append(p)
            #print(percs, 'percs')
            items: list[dict] = []
            item: dict = {}
            nig = " "
            for ai in range(len(pmsb_zeroless)):
                item_str = str(pmsb_zeroless[ai])
                item[nig] = percs[ai]
                #item[item_str] = percs[ai]
                nig += " "
                items.append(item)
            #print(items)

            skibidi = AKPieChart(
                items=items,
                #x_values=[x for x in range(len(pmsb_))],
                #labels=False,
                #bg_color=get_color_from_hex("#ffffff55")
                duration=0
            )
            self.add_widget(skibidi)


class GraphMinus(MDBoxLayout):
    def __init__(self, stocks: list = [], **kwargs):
        super(GraphMinus, self).__init__(**kwargs)
        self.stocks = stocks
        print(stocks, "graphminus")
        if stocks:
            if stocks[-1] < stocks[-2]:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(1, 0, 0, 1),
                    circles_radius="8dp",
                    lines_color=(1, 0, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
            else:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(1, 0, 0, 1),
                    circles_radius="8dp",
                    lines_color=(0, 1, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
        else:
            pass


class GraphMinus2(MDBoxLayout):
    def __init__(self, stocks: list = [], **kwargs):
        super(GraphMinus2, self).__init__(**kwargs)
        self.stocks = stocks
        print(stocks, "graphminus")
        if stocks:
            if stocks[-1] < stocks[-2]:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(1, 0, 0, 1),
                    circles_radius="8dp",
                    lines_color=(1, 0, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
            else:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(0, 1, 0, 1),
                    circles_radius="8dp",
                    lines_color=(0, 1, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
        else:
            pass


class GraphMinus3(MDBoxLayout):
    def __init__(self, stocks: list = [], **kwargs):
        super(GraphMinus3, self).__init__(**kwargs)
        self.stocks = stocks
        print(stocks, "graphminus")
        if stocks:
            if stocks[-1] < stocks[-2]:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(1, 0, 0, 1),
                    circles_radius="8dp",
                    lines_color=(1, 0, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
            else:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(0, 1, 0, 1),
                    circles_radius="8dp",
                    lines_color=(0, 1, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
        else:
            pass


class GraphMinus4(MDBoxLayout):
    def __init__(self, stocks: list = [], **kwargs):
        super(GraphMinus4, self).__init__(**kwargs)
        self.stocks = stocks
        print(stocks, "graphminus")
        if stocks:
            if stocks[-1] < stocks[-2]:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(1, 0, 0, 1),
                    circles_radius="8dp",
                    lines_color=(1, 0, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
            else:
                abobq = AKLineChart(
                    bg_color=(0, 0, 0, 0),
                    anim=False,
                    labels=False,
                    circles_color=(0, 1, 0, 1),
                    circles_radius="8dp",
                    lines_color=(0, 1, 0, 1),
                    y_values=stocks,
                    x_values=[x for x in range(len(stocks))]
                )
                self.add_widget(abobq)
        else:
            pass

#class Image1(BoxLayout):
#def __init__(self, **kwargs):
#super(Image1, self).__init__(**kwargs)
#
#with self.canvas:
#self.a = Rectangle(
#source='https://www.hdwallpapers.in/download/blue_purple_waves_shapes_gradient_4k_hd_abstract-1920x1080.jpg',
#)
#
#self.bind(pos=self.update_bg)
#self.bind(size=self.update_bg)
#
#def update_bg(self, *args):
#self.a.pos = self.pos
#self.a.size = self.size
#

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import FrostedGlass kivy_garden.frostedglass
#:import Gradient kivy_gradient.Gradient
    
MDNavigationLayout:
    MDScreenManager:
        id: sm            
        MDScreen:
            name: "stocks"
            BoxLayout:
                id: box
                canvas:
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        texture:
                            Gradient.vertical(
                            get_color_from_hex("2999ad"),
                            get_color_from_hex("31e975"),
                            get_color_from_hex("574bcd")
                            )
            FrostedGlass:
                id: frfrfr1
                background: box  
                size_hint: 1, 1
                blur_size: 5
                saturation: 1
                luminosity: 1
                overlay_color: "#05dcf033"
                noise_opacity: 0
                border_radius:  dp(0), dp(0), dp(0), dp(0)
                outline_color: "#ffffff88"
                outline_width: 1                    
                #MDTopAppBar:
                    ##title: "Navigation Drawer"
                    #duration: 0
                    #elevation: 0
                    #_no_ripple_effect: True
                    #ripple_scale: 0
                    #ripple_color: (0, 0, 0, 0)
                    ##remove_shadow: True
                    #pos_hint: {"top": 1}
                    #md_bg_color: "#e7e4c000"
                    ##specific_text_color: "#4a4939"
                    #left_action_items: [["menu", lambda x: app.open_nav()]]
                    #right_action_items: [["format-paint", lambda y: app.theme()]]                      
                #FrostedGlass:
                    ##id: frfrfr1
                    #background: box  
                    #size_hint: 1, .8
                    #pos_hint: {"top": 1}
                    #blur_size: 5
                    #saturation: 1
                    #luminosity: 1
                    #overlay_color: "#574bcd22"
                    #noise_opacity: 0.04
                    #border_radius:  dp(0), dp(0), dp(30), dp(30)
                    #outline_color: "#ffffff88"
                    #outline_width: 1            
                RecycleView:
                    do_scroll_x: True
                    do_scroll_y: False
                    size_hint: 1, .25
                    pos_hint: {"top": .93}
                    BoxLayout:
                        #id: bbb
                        #rows: 1
                        #cols: 4
                        spacing: 50
                        padding: 35
                        size_hint_x: 4
                        #Image1:
                            #id: bbb
                        FrostedGlass:
                            id: frfrfr1
                            background: box
                            size_hint: 1, 1
                            blur_size: 5
                            saturation: 1.0
                            luminosity: 1.0
                            overlay_color: "#41e97540"
                            noise_opacity: 0.04
                            border_radius:  dp(30), dp(30), dp(30), dp(30)
                            outline_color: "#ffffff"
                            outline_width: 1
                            RoundedIcon:
                                pos_hint: {"center_x": .1, "top": .9}
                                size_hint: .125, .3
                            MDLabel:
                                size_hint: .3, .2
                                text: "SBERP"
                                pos_hint: {"center_x": .35, "top": .92}
                                font_style: "H5"
                            MDBoxLayout:
                                size_hint: .5, .3
                                pos_hint: {"center_x": .27, "center_y": .3}
                                orientation: "vertical"
                                padding: 10
                                spacing: 20
                                MDLabel:
                                    id: lbl1
                                    #pos_hint: {"center_x": .2, "top": .5}
                                    font_style: "Button"
                                MDLabel:
                                    id: lbl12
                                    font_style: "Button"
                            GraphMinus:
                                id: graph2
                                pos_hint: {"center_x": .7, "center_y": .5}
                                size_hint: .4, .75
                            MDLabel:
                                size_hint: .28, .2
                                id: lbl13
                                #text: "SBERP"
                                pos_hint: {"center_x": .985, "center_y": .5}
                                font_style: "H5"
                        FrostedGlass:
                            id: frfrfr2
                            background: box
                            size_hint: 1, 1
                            blur_size: 5
                            saturation: 1.0
                            luminosity: 1.0
                            overlay_color: "#ff000066"
                            noise_opacity: 0.04
                            border_radius:  dp(30), dp(30), dp(30), dp(30)
                            outline_color: "#ffffff"
                            outline_width: 1
                            RoundedIcon2:
                                pos_hint: {"center_x": .1, "top": .9}
                                size_hint: .125, .3
                            MDLabel:
                                size_hint: .3, .2
                                text: "LKOH"
                                pos_hint: {"center_x": .35, "top": .92}
                                font_style: "H5"
                            MDBoxLayout:
                                size_hint: .5, .3
                                pos_hint: {"center_x": .27, "center_y": .3}
                                orientation: "vertical"
                                padding: 10
                                spacing: 20
                                MDLabel:
                                    id: lbl2
                                    #pos_hint: {"center_x": .2, "top": .5}
                                    font_style: "Button"
                                MDLabel:
                                    id: lbl22
                                    font_style: "Button"
                            GraphMinus2:
                                id: graph2b
                                pos_hint: {"center_x": .7, "center_y": .5}
                                size_hint: .4, .75
                            MDLabel:
                                size_hint: .28, .2
                                id: lbl23
                                pos_hint: {"center_x": .985, "center_y": .5}
                                font_style: "H5"
                        FrostedGlass:
                            id: frfrfr3
                            background: box
                            size_hint: 1, 1
                            blur_size: 5
                            saturation: 1.0
                            luminosity: 1.0
                            overlay_color: "#ffffff22" 
                            noise_opacity: 0.04
                            border_radius:  dp(30), dp(30), dp(30), dp(30)
                            outline_color: "#ffffff"
                            outline_width: 1
                            RoundedIcon3:
                                pos_hint: {"center_x": .1, "top": .9}
                                size_hint: .125, .3
                            MDLabel:
                                size_hint: .3, .2
                                text: "YDEX"
                                pos_hint: {"center_x": .35, "top": .92}
                                font_style: "H5"
                            MDBoxLayout:
                                size_hint: .5, .3
                                pos_hint: {"center_x": .27, "center_y": .3}
                                orientation: "vertical"
                                padding: 10
                                spacing: 20
                                MDLabel:
                                    id: lbl3
                                    font_style: "Button"
                                MDLabel:
                                    id: lbl32
                                    font_style: "Button"
                            GraphMinus3:
                                id: graph3b
                                pos_hint: {"center_x": .7, "center_y": .5}
                                size_hint: .4, .75
                            MDLabel:
                                size_hint: .28, .2
                                id: lbl33
                                pos_hint: {"center_x": .985, "center_y": .5}
                                font_style: "H5"
                        FrostedGlass:
                            id: frfrfr4
                            background: box
                            size_hint: 1, 1
                            blur_size: 5
                            saturation: 1.0
                            luminosity: 1.0
                            overlay_color: "#0c1bf022"
                            noise_opacity: 0.04
                            border_radius:  dp(30), dp(30), dp(30), dp(30)
                            outline_color: "#ffffff"
                            outline_width: 1
                            RoundedIcon4:
                                pos_hint: {"center_x": .1, "top": .9}
                                size_hint: .125, .3
                            MDLabel:
                                size_hint: .3, .2
                                text: "PMSBP"
                                pos_hint: {"center_x": .35, "top": .92}
                                font_style: "H5"
                            MDBoxLayout:
                                size_hint: .5, .3
                                pos_hint: {"center_x": .27, "center_y": .3}
                                orientation: "vertical"
                                padding: 10
                                spacing: 20
                                MDLabel:
                                    id: lbl4
                                    font_style: "Button"
                                MDLabel:
                                    id: lbl42
                                    font_style: "Button"
                            GraphMinus3:
                                id: graph4
                                pos_hint: {"center_x": .7, "center_y": .5}
                                size_hint: .4, .75
                            MDLabel:
                                size_hint: .28, .2
                                id: lbl43
                                pos_hint: {"center_x": .985, "center_y": .5}
                                font_style: "H5"
                        RecycleBoxLayout:
                            default_size: None, None
                            default_size_hint: None, None
                            size_hint_x: None
                            height: self.minimum_height
                            width: self.minimum_width 
                MDFillRoundFlatIconButton:
                    icon: "account-cash"
                    text: "Анализ"
                    size_hint: .7, .05
                    pos_hint: {"center_x": .5, "top": .65}
                    md_bg_color: get_color_from_hex("#00ffc888")
                    on_release: app.theme()
                #MDCard:
                    #radius: (20,)
                    #size_hint: .4, .3
                    #pos_hint: {"center_x": .225, "center_y": .4}
                    #md_bg_color: get_color_from_hex("#42e6f599")
                RoundGraph:
                    id: graph3
                    size_hint: None, None
                    pos_hint: {"center_x": .225, "center_y": .4}
                    size: dp(150), dp(150)
                MDCard:
                    radius: (20,)
                    size_hint: .5, .3
                    pos_hint: {"center_x": .725, "center_y": .4}
                    md_bg_color: get_color_from_hex("#42e6f599")
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: 20
                        padding: 20
                        MDLabel:
                            pos_hint: {"center_x": .85, "top": 1}
                            text: "Сектора"
                            size_hint: 1, .2
                        MDCard:
                            md_bg_color: get_color_from_hex("#a442f577")
                            padding: 10
                            spacing: 5
                            size_hint_y: .5
                            MDIcon:
                                icon: "oil"
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text: "Нефтегаз"
                                pos_hint: {"center_y": .5}
                        MDCard:
                            md_bg_color: get_color_from_hex("#f5426677")
                            padding: 10
                            spacing: 5
                            size_hint_y: .5
                            MDIcon:
                                icon: "solar-power"
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text: "Энергетика"
                                pos_hint: {"center_y": .5}
                        MDCard:
                            md_bg_color: get_color_from_hex("#ff590077")
                            padding: 10
                            spacing: 5
                            size_hint_y: .5
                            MDIcon:
                                icon: "bank"
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text: "Финансы"
                                pos_hint: {"center_y": .5}
                        MDCard:
                            md_bg_color: get_color_from_hex("#c800ff77")
                            padding: 10
                            spacing: 5
                            size_hint_y: .5
                            MDIcon:
                                icon: "desktop-tower-monitor"
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text: "IT сектор"
                                pos_hint: {"center_y": .5}                    
                MDBoxLayout:
                    padding: 20
                    spacing: 20
                    pos_hint: {"center_x": .5, "center_y": .15}
                    size_hint: 1, .125
                    MDCard:
                        radius: (20,)
                        md_bg_color: get_color_from_hex("#ffffff55")
                        padding: 10
                        spacing: 5
                        MDBoxLayout:
                            orientation: "vertical"
                            MDBoxLayout:
                                padding: 10
                                spacing: 30
                                pos_hint: {"top": 1} 
                                size_hint: 1, .3
                                MDIconButton:
                                    icon: "currency-usd" 
                                    pos_hint: {"x": -0.5, "top": 1} 
                                    size_hint: .5, .2
                                    ripple_scale: 0
                                MDIconButton:
                                    id: usd_
                                    size_hint: .5, .2
                                    #icon: "triangle-down"
                                    #theme_icon_color: "Custom"
                                    #icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_x": 1.5, "top": .9}
                                    halign: "right" 
                                    ripple_scale: 0
                            MDLabel:
                                id: usd_lbl
                                size_hint: 1, .7
                                halign: "left"
                                pos_hint: {"x": 0, "center_y": .3}
                    MDCard:
                        radius: (20,)
                        md_bg_color: get_color_from_hex("#ffffff55")
                        padding: 10
                        spacing: 5
                        MDBoxLayout:
                            orientation: "vertical"
                            MDBoxLayout:
                                padding: 10
                                spacing: 30
                                pos_hint: {"top": 1} 
                                size_hint: 1, .3
                                MDIconButton:
                                    icon: "currency-eur" 
                                    pos_hint: {"x": -0.5, "top": 1} 
                                    size_hint: .5, .2
                                    ripple_scale: 0
                                MDIconButton:
                                    id: eur_
                                    size_hint: .5, .2
                                    #icon: "triangle-down"
                                    #theme_icon_color: "Custom"
                                    #icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_x": 1.5, "top": .9}
                                    halign: "right" 
                                    ripple_scale: 0
                            MDLabel:
                                id: eur_lbl
                                size_hint: 1, .7
                                halign: "left"
                                pos_hint: {"x": 0, "center_y": .3}
                    MDCard:
                        radius: (20,)
                        #size_hint: .7, .09
                        md_bg_color: get_color_from_hex("#ffffff55")
                        MDBoxLayout:
                            orientation: "vertical"
                            padding: 10
                            spacing: 10
                            pos_hint: {"x": 0, "top": 1} 
                            MDIconButton:
                                icon: "currency-btc" 
                                pos_hint: {"x": 0} 
                                size_hint: .1, .3
                                ripple_scale: 0
                            MDLabel:
                                id: btc_lbl
                                size_hint: 1, .7
                                pos_hint: {"x": 0}
                    MDCard:
                        radius: (20,)
                        #size_hint: .7, .09
                        md_bg_color: get_color_from_hex("#ffffff55")
                        MDBoxLayout:
                            orientation: "vertical"
                            padding: 10
                            spacing: 10
                            pos_hint: {"x": 0, "top": 1} 
                            MDIconButton:
                                icon: "ethereum" 
                                pos_hint: {"x": 0} 
                                size_hint: .1, .3
                                ripple_scale: 0
                            MDLabel:
                                id: eth_lbl
                                size_hint: 1, .7
                                pos_hint: {"x": 0}                                    
        MDScreen:
            name: "theme"
            id: st
            MDBoxLayout:
                AsyncImage:
                    id: bbbb
                    #pos: self.pos
                    size_hint: 1, None
                    size: root.size
                    allow_stretch: True
                    keep_ratio: False
                    source: "https://oboi-download.ru/files/wallpapers/793/22154.jpg"      
                                                          
            MDTopAppBar:
                #title: "Navigation Drawer"
                duration: 0
                elevation: 0
                _no_ripple_effect: True
                ripple_scale: 0
                ripple_color: (0, 0, 0, 0)
                #remove_shadow: True
                pos_hint: {"top": 1}
                md_bg_color: "#e7e4c000"
                #specific_text_color: "#4a4939"
                #left_action_items: [["menu", lambda x: app.open_nav()]]
                left_action_items: [["arrow-left-thick", lambda y: app.back()]]
            MDBoxLayout:
                orientation: "vertical"    
                pos_hint: {"center_y": .5}
                size_hint: 1, .7
                padding: 20
                spacing: 20
                MDBoxLayout:
                    size_hint: 1, .4
                    Graph1:      
                        id: graph1
                        size_hint: .7, 2.5
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_x: .35
                        spacing: 50
                        padding: 10
                        MDCard:
                            radius: (30,)
                            size_hint: .8, .08
                            pos_hint: {"center_x": .5, "top": 1}
                            md_bg_color: get_color_from_hex("#8696ff99")
                            #line_color: get_color_from_hex("#ffffff99")
                            #line_color_width: 5
                            MDLabel:
                                id: graphl
                                font_style: "H6"
                                style: "Bold"
                                pos_hint: {"center_y": .5}
                                halign: "center"
                                adaptive_height: True                  
                        MDCard:
                            size_hint: .8, .08
                            pos_hint: {"center_x": .5, "bottom": 1}
                            radius: (30,)
                            md_bg_color: get_color_from_hex("#d1ffe799")
                            MDLabel:
                                text: "IMOEX 2758.3"
                                font_style: "H6"
                                style: "Bold"
                                pos_hint: {"center_y": .5}
                                halign: "center"
                                adaptive_height: True
                                #size_hint: .5, .5
                FrostedGlass:
                    background: bbbb
                    size_hint: 1, .6
                    blur_size: 5
                    saturation: 1
                    luminosity: 1
                    overlay_color: "#ffffff44"
                    #pos_hint: {"center_x": .5, "center_y": .5}
                    noise_opacity: 0.035
                    border_radius:  dp(30), dp(30), dp(30), dp(30)
                    outline_color: "#ffffff88"
                    outline_width: 1         
                                                                  
    #MDNavigationDrawer:
        #id: nav_drawer
        ##radius: (0, 16, 16, 0)
        #theme_bg_color: "Custom"
        #md_bg_color: get_color_from_hex("#8697ff0")
        #elevation: 0
        #scrim_color: 0, 0, 0, 0
        ##opening_time: .15
        ##closing_time: .15
        #FrostedGlass:
            #id: frgl
            #background: sm  #best match: sm
            #size_hint_y: .95
            #pos_hint: {"center_y": .5}
            #blur_size: 5
            #saturation: 1
            #luminosity: 1
            #overlay_color: "#ffffff33"
            ##overlay_color: "#ffffff55"
            #noise_opacity: 0
            #border_radius:  dp(0), dp(30), dp(30), dp(0)
            #outline_color: "#ffffff88"
            #outline_width: 2.5
                    
'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)

        self.t2 = threading.Thread(target=self.currencies)
        self.t3 = threading.Thread(target=self.crypto)
        #self.p0 = multiprocessing.Process(target=self.show_graph)

    def build(self):
        self.theme_cls.material_style = "M3"

        self.stocks: list[float] = [0, 3000, 7000, 3100, 4000]
        self.launched: bool = False

        #Clock.schedule_once(self.render, 3)

        return Builder.load_string(KV)

#
    #    headers = {'User-Agent':  heads[0]}
    #    #print(headers)
#
    #    response = requests.get(url, headers=headers)
    #    print(response.content)
    #    print(response.status_code)
#
    #    if response.status_code == 200:
    #        soup = BeautifulSoup(response.content, 'html.parser')
#
    #        price_div = soup.find('div', class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]')
#
    #        if price_div:
    #            price = price_div.text.strip()
    #            return price
    #        else:
    #            return "Price div not found."
    #    else:
    #        rand = random.choice((1, len(heads)-1))
    #        headers = {'User-Agent': heads[rand]}
    #        print(headers)
    #        session = HTMLSession()
    #        r = session.get(url, headers=headers)
    #        soup = BeautifulSoup(r.html.html, 'html.parser')
    #        result = soup.find_all('div', class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]')
    #        print(result, 'else')
    #        # print(type(result))
    #        if result:
    #            value = result[0].text.replace('\xa0', '')
    #            return value
    #        else:
    #            return 'no info for sberp'

    def theme(self):
        self.root.ids.sm.current = "theme"

    def back(self):
        self.root.ids.sm.current = "stocks"

    def sberp_(self) -> list | None:
        with requests.Session() as session:
            data = apimoex.get_market_candles(session, 'SBERP')
        if data:
            sber = str(round(data[-1]["close"], 2))
            graph: list[float] = []
            index: int = -5
            for i in range(5):
                graph.append(round(float(data[index]["close"]), 1))
                index += 1
            graphminus = GraphMinus(graph)
            self.root.ids.graph2.clear_widgets()
            self.root.ids.graph2.add_widget(graphminus)
            integer = sber[0:-2]
            integer = sber.replace(" ", "", 1)
            integer = float(integer.replace(",", ".", 1))
            #print(integer)
            self.root.ids.lbl1.text = '10 шт. - ' + str(round(integer*10)) + "₽"
            self.root.ids.lbl12.text = "308 -> " + str(integer)
            global scks
            lbl = round(integer*100/scks[0])
            lbl: int = lbl - 100
            if lbl < 100:
                self.root.ids.lbl13.theme_text_color = "Custom"
                self.root.ids.lbl13.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl13.text = str(lbl) + "%"
            elif lbl > 100:
                self.root.ids.lbl13.theme_text_color = "Custom"
                self.root.ids.lbl13.text_color = get_color_from_hex("#10eb38")
                self.root.ids.lbl13.text = "+" + str(lbl) + "%"
            else:
                self.root.ids.lbl13.theme_text_color = "Custom"
                self.root.ids.lbl13.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl13.text = "0%"
            #self.show_graph()
            #print(graph, "graph return")
            return graph
        else:
            return None

    def currencies(self):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        usd = round(float(response.json()["Valute"]["USD"]["Value"]), 2)
        usd_prev = round(float(response.json()["Valute"]["USD"]["Previous"]), 2)
        if usd:
            self.root.ids.usd_.theme_icon_color = "Custom"
            self.root.ids.usd_lbl.text = str(usd) + " ₽"
            if usd < usd_prev:
                self.root.ids.usd_.icon = "triangle-down"
                self.root.ids.usd_.icon_color = (1, 0, 0, 1)
            else:
                self.root.ids.usd_.icon = "triangle"
                self.root.ids.usd_.icon_color = (0, 1, 0, 1)
        else:
            self.root.ids.usd_.icon = "cloud-question"
        eur = round(float(response.json()["Valute"]["EUR"]["Value"]), 2)
        eur_prev = round(float(response.json()["Valute"]["EUR"]["Previous"]), 2)
        if eur:
            self.root.ids.eur_.theme_icon_color = "Custom"
            self.root.ids.eur_lbl.text = str(eur) + " ₽"
            if eur < eur_prev:
                self.root.ids.eur_.icon = "triangle-down"
                self.root.ids.eur_.theme_icon_color = "Custom"
                self.root.ids.eur_.icon_color = (1, 0, 0, 1)
            else:
                self.root.ids.eur_.icon = "triangle"
                self.root.ids.eur_.theme_icon_color = "Custom"
                self.root.ids.eur_.icon_color = (0, 1, 0, 1)
        else:
            self.root.ids.eur_.icon = "cloud-question"

    def crypto(self):
        url1 = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        url2 = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        btc = round(float(response1.json()['price']))
        #print(btc)
        eth = round(float(response2.json()['price']))
        if btc:
            #self.root.ids.btc_.theme_icon_color = "Custom"
            self.root.ids.btc_lbl.text = f"{btc}$"
        else:
            self.root.ids.btc_.icon = "cloud-question"
        if eth:
            self.root.ids.eth_lbl.text = f"{eth}$"
        else:
            self.root.ids.eth_.icon = "cloud-question"

    def show_graph(self):
        #print(self.root.ids.cl.children)
        #print(self.root.ids.frgl.children)
        graph1 = Graph1(self.stocks)
        self.root.ids.graph1.clear_widgets()
        self.root.ids.graph1.add_widget(graph1)
        self.root.ids.graphl.text = "Баланс: " + str(sum(self.stocks)) + '₽'
        #graphminus = GraphMinus(graph)
        #self.root.ids.graph2.clear_widgets()
        #self.root.ids.graph2.add_widget(graphminus)
        self.t2.start()
        self.t3.start()
        graph = self.sberp_()
        graphminus = GraphMinus(graph)
        self.root.ids.graph2.clear_widgets()
        self.root.ids.graph2.add_widget(graphminus)
        graph2 = self.lkoh_()
        graphlkoh = GraphMinus2(graph2)
        self.root.ids.graph2b.clear_widgets()
        self.root.ids.graph2b.add_widget(graphlkoh)
        graph3 = self.ydex_()
        graphlkoh = GraphMinus3(graph3)
        self.root.ids.graph3b.clear_widgets()
        self.root.ids.graph3b.add_widget(graphlkoh)
        graph4 = self.pmsbp_()
        graphlkoh = GraphMinus4(graph4)
        self.root.ids.graph4.clear_widgets()
        self.root.ids.graph4.add_widget(graphlkoh)
        #print(self.show_graph, "show")
        #self.root.ids.frgl.clear_widgets()
        #self.t1.start()
        #self.p.close()

    def round_graph(self):
        graph3 = RoundGraph(self.stocks)
        self.root.ids.graph3.clear_widgets()
        self.root.ids.graph3.add_widget(graph3)

    #def open_nav(self):
        #self.root.ids.frgl.clear_widgets()
    #    self.root.ids.nav_drawer.set_state("open")
    #    print(self.root.ids.nav_drawer.state)
        #Clock.schedule_once(self.show_graph, 0.16)
        #Clock.schedule_interval(self.closee, 0.1)

    #def imoex(self):
    #    url = "https://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics/IMOEX.json?iss.meta=off&limitt=100"
    #    with requests.Session() as session:
    #        data = apimoex.get_board_history(session, "")

    def lkoh_(self) -> list | None:
        with requests.Session() as session:
            data = apimoex.get_market_candles(session, 'LKOH')
        if data:
            lkoh = str(round(data[-1]["close"], 2))
            graph: list[float] = []
            index: int = -5
            for i in range(5):
                graph.append(round(float(data[index]["close"]), 1))
                index += 1
            graphminus = GraphMinus2(graph)
            self.root.ids.graph2b.clear_widgets()
            self.root.ids.graph2b.add_widget(graphminus)
            integer = lkoh[0:-2]
            integer = lkoh.replace(" ", "", 1)
            integer = float(integer.replace(",", ".", 1))
            #print(integer)
            self.root.ids.lbl2.text = '1 шт. - ' + str(integer) + "₽"
            self.root.ids.lbl22.text = "6600 -> " + str(integer)
            global scks
            lbl = round(integer*100/scks[1])
            lbl: int = lbl - 100
            if lbl < 100:
                self.root.ids.lbl23.theme_text_color = "Custom"
                self.root.ids.lbl23.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl23.text = str(lbl) + "%"
            elif lbl > 100:
                self.root.ids.lbl23.theme_text_color = "Custom"
                self.root.ids.lbl23.text_color = get_color_from_hex("#10eb38")
                self.root.ids.lbl23.text = "+" + str(lbl) + "%"
            else:
                self.root.ids.lbl23.theme_text_color = "Custom"
                self.root.ids.lbl23.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl23.text = "0%"
            #self.show_graph()
            #print(graph, "graph return")
            return graph
        else:
            return None

    def ydex_(self) -> list | None:
        with requests.Session() as session:
            data = apimoex.get_market_candles(session, 'YDEX')
        if data:
            ydex = str(round(data[-1]["close"], 2))
            graph: list[float] = []
            index: int = -5
            for i in range(5):
                graph.append(round(float(data[index]["close"]), 1))
                index += 1
            graphminus = GraphMinus3(graph)
            self.root.ids.graph3b.clear_widgets()
            self.root.ids.graph3b.add_widget(graphminus)
            integer = ydex[0:-2]
            integer = ydex.replace(" ", "", 1)
            integer = float(integer.replace(",", ".", 1))
            #print(integer)
            self.root.ids.lbl3.text = '1 шт. - ' + str(integer) + "₽"
            self.root.ids.lbl32.text = "3900 -> " + str(integer)
            global scks
            lbl = round(integer*100/scks[2])
            lbl: int = lbl - 100
            if lbl < 100:
                self.root.ids.lbl33.theme_text_color = "Custom"
                self.root.ids.lbl33.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl33.text = str(lbl) + "%"
            elif lbl > 100:
                self.root.ids.lbl33.theme_text_color = "Custom"
                self.root.ids.lbl33.text_color = get_color_from_hex("#10eb38")
                self.root.ids.lbl33.text = "+" + str(lbl) + "%"
            else:
                self.root.ids.lbl33.theme_text_color = "Custom"
                self.root.ids.lbl33.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl33.text = "0%"
            #self.show_graph()
            #print(graph, "graph return")
            return graph
        else:
            return None

    def pmsbp_(self) -> list | None:
        with requests.Session() as session:
            data = apimoex.get_market_candles(session, 'PMSBP')
        if data:
            pmsbp = str(round(data[-1]["close"], 2))
            graph: list[float] = []
            index: int = -5
            for i in range(5):
                graph.append(round(float(data[index]["close"]), 1))
                index += 1
            graphminus = GraphMinus4(graph)
            self.root.ids.graph4.clear_widgets()
            self.root.ids.graph4.add_widget(graphminus)
            integer = pmsbp[0:-2]
            integer = pmsbp.replace(" ", "", 1)
            integer = float(integer.replace(",", ".", 1))
            #print(integer)
            self.root.ids.lbl4.text = '10 шт. - ' + str(round(integer*10)) + "₽"
            self.root.ids.lbl42.text = "2800 -> " + str(integer)
            global scks
            lbl = round(integer*100/scks[3])
            lbl: int = lbl - 100
            if lbl < 100:
                self.root.ids.lbl43.theme_text_color = "Custom"
                self.root.ids.lbl43.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl43.text = str(lbl) + "%"
            elif lbl > 100:
                self.root.ids.lbl43.theme_text_color = "Custom"
                self.root.ids.lbl43.text_color = get_color_from_hex("#10eb38")
                self.root.ids.lbl43.text = "+" + str(lbl) + "%"
            else:
                self.root.ids.lbl43.theme_text_color = "Custom"
                self.root.ids.lbl43.text_color = get_color_from_hex("#fc0b03")
                self.root.ids.lbl43.text = "0%"
            #self.show_graph()
            #print(graph, "graph return")
            return graph
        else:
            return None

    def on_start(self):
        if platform == "android":
            from android.permissions import request_permissions, Permission

            request_permissions(
                [Permission.INTERNET,
                 Permission.READ_EXTERNAL_STORAGE,
                 Permission.WRITE_EXTERNAL_STORAGE,
                 Permission.ACCESS_NETWORK_STATE]
            )

        #t = Thread(target=self.open_nav, daemon=Thread)
        #t1 = threading.Thread(target=self.sberp_)
        #t1.start()
        #self.sberp_()
        self.round_graph()
        #Clock.schedule_once(self.show_graph, 5)
        #self.r4 = threading.Thread(target=self.imoex)
        #t2 = threading.Thread(target=self.lkoh_)
        #t3 = threading.Thread(target=self.ydex_())
        #t4 = threading.Thread(target=self.pmsbp_())
        #t2.start()
        #t3.start()
        #t4.start()
        self.fps_monitor_start()
        self.show_graph()
        #self.p0.start()
        #p.terminate()


if __name__ == "__main__":
    Example().run()
