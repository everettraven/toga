import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, GLib

# The following import will fail if WebKit or its API wrappers aren't
# installed; handle failure gracefully
# (see https://github.com/beeware/toga/issues/26)
# Accept any API version greater than 3.0
WebKit2 = None
for version in ['4.0', '3.0']:
    try:
        gi.require_version('WebKit2', version)
        from gi.repository import WebKit2
        break
    except (ImportError, ValueError):
        pass

try:
    gi.require_version("Pango", "1.0")
    from gi.repository import Pango
except ImportError:
    Pango = None

try:
    import cairo
except ImportError:
    cairo = None
