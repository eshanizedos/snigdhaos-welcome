# =================================================================
# =          Authors: Brad Heffernan & Erik Dubois                =
# =================================================================

import os
import getpass
from os.path import expanduser

DEBUG = False
#DEBUG = True

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()

if DEBUG:
    user = username
else:
    user = "liveuser"

Settings = home + "/.config/snigdhaos-welcome/settings.conf"
Skel_Settings = "/etc/skel/.config/snigdhaos-welcome/settings.conf"
dot_desktop = "/usr/share/applications/snigdhaos-welcome.desktop"
autostart = home + "/.config/autostart/snigdhaos-welcome.desktop"


def GUI(self, Gtk, GdkPixbuf):

    autostart = eval(self.load_settings())

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    infoE = Gtk.EventBox()
    pbinfo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/question.png'), 38, 38)
    infoimage = Gtk.Image().new_from_pixbuf(pbinfo)
    infoE.add(infoimage)
    infoE.connect("button_press_event", self.on_info_clicked)
    infoE.set_property("has-tooltip", True)
    infoE.connect("query-tooltip", self.tooltip_callback, "Conflicts Info")

    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>Welcome to <b>Snigdha OS (HawkEye)</b></big>")
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    label_warning = Gtk.Label(xalign=0)
    label_warning.set_justify(Gtk.Justification.CENTER)
    label_warning.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "Clean the computer with <b>Gparted</b> before installing.\n" +
            # "During the Calamares installation many options will be open to you. You have the freedom of choice.\n" +  # noqa
            # "We communicate with our community via a diversity of social media." +  # noqa
            # "Do join us to learn the latest news, ask questions or for casual talk.\n" +  # noqa
            # "<b>Telegram</b> is for chitchat - <b>Discord</b> is for assistance.\n" +  # noqa
            "We have a <b>forum</b> for the longer and more technical questions.\n")
        label_warning.set_markup(
            "\n<span size='x-large'><b>Use the Offline Installation\n" + # noqa
            "if the Online Installation fails</b></span>\n")  # noqa
    else:
        label2.set_markup("The links below will get you started on Snigdha OS. We communicate with our community via Forum.\n"
                          "Do join us to learn the latest news, ask questions or for casual talk.\n" +  # noqa
                          "<b>Telegram</b> is for chitchat - <b>Discord</b> is for assistance.\n" +  # noqa
                          "We have a <b>forum</b> for the longer and more technical questions.\n" +  # noqa
                          "Learn, have fun and enjoy.")

    hbox4.set_center_widget(label2)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    #hbox4.pack_start(label2, False, False, 0)
    hbox8.pack_start(label_warning, True, False, 0)

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 80)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Offline Installation</b></span>")

    button2.connect("clicked", self.on_ai_clicked)
    button2.set_size_request(0, 80)

    buttonca = Gtk.Button(label="")
    buttonca_label = buttonca.get_child()
    buttonca_label.set_markup("<span size='large'><b>Online Installation</b></span>")

    buttonca.connect("clicked", self.on_aica_clicked)
    buttonca.set_size_request(0, 80)


    self.button8 = Gtk.Button(label="")
    button8_label = self.button8.get_child()
    button8_label.set_markup("<span size='large'><b>Update Mirrors</b></span>")
    self.button8.connect("clicked", self.on_mirror_clicked)
    self.button8.set_size_request(420, 70)

    self.buttonatt = Gtk.Button(label="")
    buttonatt_label = self.buttonatt.get_child()
    buttonatt_label.set_markup("<span size='large'><b>Launch Arch Linux Tweak Tool</b></span>")
    self.buttonatt.connect("clicked", self.on_buttonatt_clicked)
    self.buttonatt.set_size_request(420, 70)

    self.buttonpamac = Gtk.Button(label="")
    buttonpamac_label = self.buttonpamac.get_child()
    buttonpamac_label.set_markup("<span size='large'><b>Install software</b></span>")
    self.buttonpamac.connect("clicked", self.on_buttonpamac_clicked)
    self.buttonpamac.set_size_request(420, 70)

    # grid.add(button1)
    if username == user:
        grid = Gtk.Grid()
        grid.attach(self.button8, 2, 0, 2, 2)
        #grid.attach(button13, 2, 0, 2, 2)
        grid.attach(button1, 2, 2, 2, 2)
        grid.attach(button2, 1, 4, 2, 2)
        grid.attach(buttonca, 3, 4, 2, 2)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
    else:
        grid = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.button8.set_size_request(300, 70)
        self.buttonatt.set_size_request(300, 70)
        self.buttonpamac.set_size_request(300, 70)
        grid.pack_start(self.buttonpamac, True, False, 0)
        grid.pack_start(self.buttonatt, True, False, 0)
        grid.pack_start(self.button8, True, False, 0)
    # grid.set_row_homogeneous(True)

    # ======================================================================
    #                   NOTICE
    # ======================================================================

    # label3 = Gtk.Label(xalign=0)
    # label3.set_line_wrap(True)

    # label4 = Gtk.Label(xalign=0)
    # label4.set_line_wrap(True)

    # self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # self.vbox2.pack_start(label3, False,False,0)
    # self.vbox2.pack_start(label4, False,False,0)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("snigdha  |")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("<i>No Password</i>")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================

    # change this one every year
    button3 = Gtk.Button(label="Release info")
    button3.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")
    button3.set_size_request(180, 50)

    button4 = Gtk.Button(label="Choose your project")
    button4.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")
    button4.set_size_request(180, 50)

    button5 = Gtk.Button(label="Core info")
    button5.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")
    button5.set_size_request(180, 50)

    button6 = Gtk.Button(label="Fast track")
    button6.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")
    button6.set_size_request(180, 50)

    button7 = Gtk.Button(label="Forum")
    button7.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")
    button7.set_size_request(180, 50)

    button70 = Gtk.Button(label="Screen resolution")
    button70.set_size_request(180, 50)
    button70.set_property("has-tooltip", True)
    button70.connect("query-tooltip",
                      self.tooltip_callback,
                      "Launch Arandr")
    button70.connect("clicked", self.on_buttonarandr_clicked)

    hbox2.pack_start(button3, True, True, 0)
    hbox2.pack_start(button4, True, True, 0)
    hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)
    hbox2.pack_start(button70, True, True, 0)

    button8 = Gtk.Button(label="")
    button8_label = button8.get_child()
    button8_label.set_markup("<b>Donate</b>")
    button8.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")

    button9 = Gtk.Button(label="Get Involved - Betatester")
    button9.connect("clicked", self.on_link_clicked,
                    "https://eshanizedos.github.io/")

    button10 = Gtk.Button(label="Get Involved - AAG")
    button10.connect("clicked", self.on_link_clicked,
                     "https://eshanizedos.github.io/")

    button11 = Gtk.Button(label="Youtube")
    button11.connect("clicked", self.on_link_clicked,
                     "#")

    button12 = Gtk.Button(label="Exit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)
    #button12.set_tooltip_markup("Quit the ArcoLinux Welcome App")

    hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)
    hbox5.pack_start(button12, True, True, 0)


    # hbox8.pack_start(self.button8, True, False, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================

    check = Gtk.CheckButton(label="Autostart")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)

    # ======================================================================
    #                   SOCIAL LINKS
    # ======================================================================
    fbE = Gtk.EventBox()
    tE = Gtk.EventBox()
    meE = Gtk.EventBox()
    inE = Gtk.EventBox()
    liE = Gtk.EventBox()
    pE = Gtk.EventBox()
    yE = Gtk.EventBox()
    dE = Gtk.EventBox()
    tgE = Gtk.EventBox()
    elE = Gtk.EventBox()

    pbfb = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/facebook.png'), 28, 28)
    fbimage = Gtk.Image().new_from_pixbuf(pbfb)

    pbt = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/twitter.png'), 28, 28)
    timage = Gtk.Image().new_from_pixbuf(pbt)

    pbme = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/mewe.png'), 23, 23)
    meimage = Gtk.Image().new_from_pixbuf(pbme)

    pbin = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/insta.png'), 28, 28)
    inimage = Gtk.Image().new_from_pixbuf(pbin)

    pbli = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/linkedin.png'), 28, 28)
    liimage = Gtk.Image().new_from_pixbuf(pbli)

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/patreon.png'), 28, 28)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pby = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/youtube.png'), 28, 28)
    yimage = Gtk.Image().new_from_pixbuf(pby)

    pbd = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/discord.png'), 28, 28)
    dimage = Gtk.Image().new_from_pixbuf(pbd)

    pbtg = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/tg.png'), 28, 28)
    tgimage = Gtk.Image().new_from_pixbuf(pbtg)

    pbel = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/element.png'), 28, 28)
    elimage = Gtk.Image().new_from_pixbuf(pbel)

    fbE.add(fbimage)
    tE.add(timage)
    meE.add(meimage)
    inE.add(inimage)
    liE.add(liimage)
    pE.add(pimage)
    yE.add(yimage)
    dE.add(dimage)
    tgE.add(tgimage)
    elE.add(elimage)

    fbE.connect("button_press_event", self.on_social_clicked,
                "https://www.facebook.com/eshanized")
    tE.connect("button_press_event", self.on_social_clicked,
               "https://twitter.com/eshanized")
    meE.connect("button_press_event", self.on_social_clicked,
                "#")
    inE.connect("button_press_event", self.on_social_clicked,
                "https://www.instagram.com/eshanized/")
    liE.connect("button_press_event", self.on_social_clicked,
                "https://www.linkedin.com/in/eshanized/")
    pE.connect("button_press_event", self.on_social_clicked,
               "https://www.patreon.com/eshanized")
    yE.connect("button_press_event", self.on_social_clicked,
               "https://youtube.com/c/eshanized")
    dE.connect("button_press_event", self.on_social_clicked,
               "#")
    tgE.connect("button_press_event", self.on_social_clicked,
                "#")
    elE.connect("button_press_event", self.on_social_clicked,
                "#")

    fbE.set_property("has-tooltip", True)
    tE.set_property("has-tooltip", True)
    meE.set_property("has-tooltip", True)
    inE.set_property("has-tooltip", True)
    liE.set_property("has-tooltip", True)
    pE.set_property("has-tooltip", True)
    yE.set_property("has-tooltip", True)
    dE.set_property("has-tooltip", True)
    tgE.set_property("has-tooltip", True)
    elE.set_property("has-tooltip", True)

    fbE.connect("query-tooltip", self.tooltip_callback, "Facebook")
    tE.connect("query-tooltip", self.tooltip_callback, "Twitter")
    meE.connect("query-tooltip", self.tooltip_callback, "Mewe")
    inE.connect("query-tooltip", self.tooltip_callback, "Instagram")
    liE.connect("query-tooltip", self.tooltip_callback, "LinkedIn")
    pE.connect("query-tooltip", self.tooltip_callback, "Patreon")
    yE.connect("query-tooltip", self.tooltip_callback, "Youtube")
    dE.connect("query-tooltip", self.tooltip_callback, "Discord")
    tgE.connect("query-tooltip", self.tooltip_callback, "Telegram")
    elE.connect("query-tooltip", self.tooltip_callback, "Element-Matrix")

    hbox3.pack_start(fbE, False, False, 0)
    hbox3.pack_start(tE, False, False, 0)
    hbox3.pack_start(meE, False, False, 0)
    hbox3.pack_start(inE, False, False, 0)
    hbox3.pack_start(liE, False, False, 0)
    hbox3.pack_start(elE, False, False, 0)

    hbox6.pack_start(pE, False, False, 50)
    hbox6.pack_start(yE, False, False, 0)
    hbox6.pack_start(dE, False, False, 0)
    hbox6.pack_start(tgE, False, False, 0)
    if username == user:
        hbox3.pack_start(hboxUser, True, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   Start Arcolinux Tweak Tool
    # ======================================================================
    launchBox = Gtk.EventBox()
    pblaunch = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/archlinux-tweak-tool.svg'), 40, 40)
    launchimage = Gtk.Image().new_from_pixbuf(pblaunch)

    launchBox.add(launchimage)
    launchBox.connect("button_press_event", self.on_launch_clicked, "")

    launchBox.set_property("has-tooltip", True)
    launchBox.connect("query-tooltip",
                      self.tooltip_callback,
                      "Launch Arch Linux Tweak Tool")

    hbox6.pack_start(launchBox, False, False, 0)
    #hbox6.pack_start(infoE, False, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    label3 = Gtk.Label("v20.6-4")
    hbox7.pack_end(label3, False, False, 0)
    # if self.is_connected():
    #     self.get_message(label3, label4)

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label
    self.vbox.pack_start(hbox8, False, False, 7)  # warning Label

    self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares

    # if self.results and self.is_connected():
    #     self.vbox.pack_start(self.vbox2, False, False, 0)  # Notice

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    #self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
