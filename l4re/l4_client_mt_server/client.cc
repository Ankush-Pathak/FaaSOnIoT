#include <l4/sys/err.h>
#include <l4/sys/types.h>
#include <l4/re/env>
#include <l4/re/util/cap_alloc>

#include <stdio.h>
#include "rpc_decl.h"

int main() 
{
    printf("Welcome to client\n");
    L4::Cap<Add> server = L4Re::Env::env()->get_cap<Add>("mtadd_server");
    if(!server.is_valid())
    {
        printf("Could not get server capability.\n");
        return 1;
    }
    l4_uint32_t val1 = 4;
    l4_uint32_t val2 = 8;
    printf("Asking for %d + %d\n", val1, val2);
    if(server->add(val1, val2, &val1)) 
    {
        printf("Error when talking to server\n");
        return 1;
    }
    printf("Result: %d\n", val1);
    return 0;
}
