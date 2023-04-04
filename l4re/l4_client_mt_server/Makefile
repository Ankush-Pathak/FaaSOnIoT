PKGDIR ?= .
L4DIR  ?= ../l4re-base-22.04.0/src/l4

TARGET               = ank_server ank_client
SRC_CC_ank_server    = server.cc
SRC_CC_ank_client    = client.cc
REQUIRES_LIBS        = cxx_libc_io cxx_io libpthread
DEPENDS_PKGS         = $(REQUIRES_LIBS)

include $(L4DIR)/mk/prog.mk
