Title: How to Install Krita in Fedora
Date: 7/14/2016, 3:52:24 PM
Category: linux, install, apps, krita, tips

In this quick tips, I want to show you how to install Krita in Fedora (and other distro as well) in a very easy steps. As you know the latest Krita now using [appimage](http://appimage.org/) for universal linux distribution.

- First we need to make directory for krita, I prefer in `/opt/krita-app/`.
```bash
# make directory
sudo mkdir /opt/krita-app/

# give permission to directory
sudo chown -R <your-username-here>:nogroup /opt/krita-app/
```

-  Now we can download krita appimage from official website [krita.org](https://krita.org/en/download/krita-desktop/), or using below script to download directly to `/opt/krita-app/`
```bash
# download krita
wget -c -P /opt/krita-app/ http://files.kde.org/krita/3/linux/krita-3.0-x86_64.appimage
```

- After download has finished, we can rename and link the krita appimage to `/usr/local` or any `$PATH`, so we can call it directly.
```bash
# rename krita appimage
mv /opt/krita-app/krita-3.0-x86_64.appimage /opt/krita-app/krita.appimage

# link to /usr/local/
sudo ln -s /opt/krita-app/krita.appimage /usr/local/bin/krita

# make sure to mark executable for it
sudo chmod +x /usr/local/bin/krita
```

- After this last step, we can call krita from terminal or create `.desktop` file for it.
- As additional here's I paste my `.desktop` file in `$HOME/.local/share/applications/krita.desktop`
```text
[Desktop Entry]                                                                    
Name=Krita
Exec=krita %U
GenericName=Digital Painting
MimeType=application/x-krita;image/openraster;application/x-krita-paintoppreset;
Comment=Digital Painting
Type=Application
Icon=krita
Categories=Qt;KDE;Graphics;
X-KDE-ServiceTypes=Calligra/Application
X-Calligra-DefaultMimeTypes=application/x-krita
X-KDE-NativeMimeType=application/x-krita
X-KDE-ExtraNativeMimeTypes=
StartupNotify=true
X-DBUS-StartupType=Multi
X-DBUS-ServiceName=org.krita.krita
X-Krita-Version=30
```

_Hope you find this post useful._
