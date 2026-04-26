# Firefox RPM for Sailfish OS

Borrowed from n2klb:
https://github.com/n2klb/firefox


### Installation


### Build

# install the [Platform SDK](https://sailfishos.org/wiki/Platform_Development).
Also install the tooling and the target(s) that you need.

# open the chroot of the SDK:
```shell
  $ /srv/mer/sdks/sfossdk/mer-sdk-chroot
```

# enter ScratchBox2 in the target of your preference:
```shell
  $ sb2 -t SailfishOS-aarch64
  $ sb2 -t SailfishOS-armv7hl
  $ sb2 -t SailfishOS-i486
```

# cd to the directory of this repo:
```shell
  $ cd RPMS/directory/
```

# enter Scratchbox2 and run rpmbuild for building the "dumb" way:
```shell
  $ rpmbuild --define "_topdir `pwd`" --define "_sourcedir `pwd`" --define "_target_cpu aarch64" -bb *.spec
  $ rpmbuild --define "_topdir `pwd`" --define "_sourcedir `pwd`" --define "_target_cpu armv7hl" -bb *.spec
  $ rpmbuild --define "_topdir `pwd`" --define "_sourcedir `pwd`" --define "_target_cpu i486" -bb *.spec
```

Setting target to i486 instead of i586 for the Jolla Tablet:
```shell
  $ rpmbuild --define "_topdir `pwd`" --define "_sourcedir `pwd`" --define "_target_cpu i486" -bb *.spec
```


## Installing extra packages
# enter ScratchBox2 root shell in sdk-install mode for installing packages that are needed to build:
```shell
  $ sb2 -t SailfishOS-aarch64 -m sdk-install -R
  $ sb2 -t SailfishOS-armv7hl -m sdk-install -R
  $ sb2 -t SailfishOS-i486 -m sdk-install -R
```

You can now use zypper to install a package, for example make:
```shell
  # zypper install make
```

Or use rpm itself to install a local package
```shell
  # rpm -Uvh RPMS/armv7hl/packagename.rpm
```

After installing packages, exit Scratchbox2 and enter Scratchbox2 in the usual way to start the build.


### Build Order

https://github.com/abranson/atk
https://github.com/abranson/libepoxy
https://github.com/n2klb/gtk


### Build Requirements

# Firefox 91 esr needs:
needs updated patch1, patch4
Rust 1.51
gtk3
atk
libepoxy

# Firefox 102 esr needs:
needs updated patch1, patch4
Rust 1.59
cbindgen 0.23.0

# Firefox 115 esr needs:
needs updated patch1, patch4
Rust 1.66
cbindgen 0.24.3

# Firefox 131 needs:
Rust 1.76

# Firefox 136 needs:
Rust 1.76

# Firefox 140 esr needs:
Rust 1.85


# SailfishOS-5.0.0.62 provides:
Rust 1.75
cbindgen 0.19
nspr 4.35
nss 3.101


### SFDK:

https://docs.sailfishos.org/Tools/Sailfish_SDK/Building_packages/

sfdk config --push target SailfishOS-5.0.0.62-aarch64

sfdk build

