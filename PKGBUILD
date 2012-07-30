#
# Apps Packages for Chakra, part of chakra-project.org
# 
# Maintainer: george <george[at]chakra-project.org>

pkgname=kapudan
pkgver=20120730
pkgrel=1
pkgdesc="Chakra's desktop greeter, a fork of Pardus's Kaptan."
arch=('i686' 'x86_64')
url='http://gitorious.org/chakra/kapudan/'
screenshot=''
license=('GPLv2')
conflicts=('kapudan-git')
depends=('python2' 'kde-baseapps-konsole' 'kde-runtime'
        'kdebindings-pykde4' 'pyqt' 'python2-xlib'
        'python2-v4l2capture' 'python-imaging')
optdepends=('spun: update notifications')

#build() {
#    cd "${srcdir}/${pkgname}-${pkgver}"
#    python2 setup.py build
#}

package() {
#   cd "${srcdir}/${pkgname}-${pkgver}"
    cd "${srcdir}/.."
    python2 setup.py install --root="${pkgdir}" --prefix="/usr"
    install -Dm755 kapudan-rootactions "${pkgdir}/usr/bin/"
}
