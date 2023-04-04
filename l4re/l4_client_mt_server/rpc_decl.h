#pragma once

#include <l4/sys/capability>
#include <l4/sys/cxx/ipc_iface>

struct Add : L4::Kobject_t<Add, L4::Kobject, 0x44>
{
  L4_INLINE_RPC(int, add, (l4_uint32_t a, l4_uint32_t b, l4_uint32_t *res));
  typedef L4::Typeid::Rpcs<add_t> Rpcs;
};
