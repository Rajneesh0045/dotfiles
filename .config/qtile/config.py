# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from typing import List, Text  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

#Colors
color_dark = ['#040417', '#191925', '#606060']
color_light = ['#eeeeee', '#9658ad', '#4965bf', '#b678cd']
color_border = ['#403069', '#A080ff', '#8080ff']


# methods/functions to call
#TODO

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "q", lazy.spawn('/home/rajneesh/prompt.sh "Are you sure to shutdown" "shutdown -h now"') , desc="Shutdown Machine"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn rofi"),
    Key([mod], "p", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn rofi"),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack=color_border[2], border_focus=color_border[1], border_normal=color_border[0], border_width=6, margin= 8),
    layout.Max(border_focus=color_border[1], border_normal=color_border[0], border_width=6, margin= 8),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=color_border[1], border_normal=color_border[0], border_width=6, margin= 8),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(border_focus=color_border[1], border_normal=color_border[0], border_width= 6, margin= 8),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
];

widget_defaults = dict(
    font='cera pro medium',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = '~/wallpapers/mint/mint.png',
        wallpaper_mode = 'fill',
        top=bar.Bar(
            [
                widget.Image(filename='~/.config/qtile/python-logo.png', margin_x=12, margin_y=6),
                widget.GroupBox(
                    font='cera pro bold',
                    active=color_light[0],
                    inactive=color_dark[2],
                    borderwidth=3,
                    margin_x=0,
                    padding_x=12,
                    highlight_method='line',
                    highlight_color=[color_dark[0], color_dark[0]],
                    this_current_screen_border=color_light[1],
                    this_screen_border=color_light[1],
                    disable_drag=True
                ),
                # widget.Prompt(),
                widget.WindowName(foreground= color_light[3], margin_x=12),
                # widget.Chord(
                #     chords_colors={
                #         'launch': ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                widget.TextBox(
                       text = '',
                       background = color_dark[1],
                       foreground = color_light[1],
                       padding = 0,
                       fontsize = 65
                ),
                widget.TextBox(text=' ', font='mononoki Nerd Font', background= color_light[1], fontsize='24', foreground= color_light[0]),
                widget.PulseVolume(background=color_light[1]),
                widget.TextBox(
                       text = '',
                       background = color_light[1],
                       foreground = color_light[2],
                       padding = 0,
                       fontsize = 65
                ),
                widget.TextBox(text=' ', font='mononoki Nerd Font', background= color_light[2], fontsize='24', foreground= color_light[0]),
                widget.Backlight(format='{percent:2.0%}', backlight_name='amdgpu_bl0', background= color_light[2], foreground= color_light[0]),
                widget.TextBox(
                       text = '',
                       background = color_light[2],
                       foreground = color_light[1],
                       padding = 0,
                       fontsize = 65
                ),
                widget.TextBox(text=' ', font='mononoki Nerd Font', background= color_light[1], fontsize='24', foreground= color_light[0]),
                widget.CPU(format='{load_percent}%', background= color_light[1], foreground= color_light[0]),
                widget.TextBox(
                       text = '',
                       background = color_light[1],
                       foreground = color_light[2],
                       padding = 0,
                       fontsize = 65
                ),
                widget.Battery(charge_char='', discharge_char='', empty_char='', format='{char}  {percent:2.0%}', background = color_light[2], notify_below=20, foreground= color_light[0]),
                widget.TextBox(
                       text = '',
                       background = color_light[2],
                       foreground = color_light[1],
                       padding = 0,
                       fontsize = 65
                ),
                widget.Clock(format=' %d %a      %I:%M %p', background= color_light[1], foreground= color_light[0]),
                widget.TextBox(
                       text = '',
                       background = color_light[1],
                       foreground = color_light[2],
                       padding = 0,
                       fontsize = 65
                       ),
                widget.CurrentLayoutIcon(scale=0.6, background= color_light[2], foreground= color_light[0]),
                widget.CurrentLayout(background= color_light[2], foreground= color_light[0]),
            ],
            30,
            background= color_dark[1],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"