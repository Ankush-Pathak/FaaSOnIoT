#include <pthread-l4.h>
#include <unistd.h>
#include <stdio.h>

#include <l4/re/env>
#include <l4/re/util/cap_alloc>
#include <l4/re/util/object_registry>
#include <l4/re/util/br_manager>
#include <l4/sys/cxx/ipc_epiface>
#include <l4/sys/ipc.h>



#include "rpc_decl.h"

static L4Re::Util::Registry_server<L4Re::Util::Br_manager_hooks> server;

static pthread_t thread2;
static void *server_thread(void *arg)
{
    l4_msgtag_t tag;
    l4_umword_t label;
    int ipc_error;
    (void) arg;
    tag = l4_ipc_wait(l4_utcb(), &label, L4_IPC_NEVER);
    while(1) 
    {
        ipc_error = l4_ipc_error(tag, l4_utcb());
        if(ipc_error)
        {
            fprintf(stderr, "Server thread IPC error: %x\n", ipc_error);
            tag = l4_ipc_wait(l4_utcb(), &label, L4_IPC_NEVER);
            continue;
        }
        printf("Thread adding: %ld + %ld\n", l4_utcb_mr()->mr[0], l4_utcb_mr()->mr[1]);
        l4_utcb_mr()->mr[0] = l4_utcb_mr()->mr[0] + l4_utcb_mr()->mr[1];

        tag = l4_ipc_reply_and_wait(l4_utcb(), l4_msgtag(0, 1, 0, 0), &label, L4_IPC_NEVER);
    }

    return NULL;
}


class MTAdd_server: public L4::Epiface_t<MTAdd_server, Add>
{
public:
    int op_add(Add::Rights, l4_uint32_t a, l4_uint32_t b, l4_uint32_t &res)
    {
        l4_utcb_mr()->mr[0] = a;
        l4_utcb_mr()->mr[1] = b;
        l4_msgtag_t tag = l4_ipc_call(pthread_l4_cap(thread2), l4_utcb(), l4_msgtag(0, 2, 0, 0), L4_IPC_NEVER);
        int ipc_error = l4_ipc_error(tag, l4_utcb());
        if(ipc_error)
            fprintf(stderr, "IPC error: %x\n", ipc_error);
        else
            printf("Received: %ld\n", l4_utcb_mr()->mr[0]);
        res = l4_utcb_mr()->mr[0];
        return 0;
    }
};

int main(void)
{
    if(pthread_create(&thread2, NULL, server_thread, NULL))
    {
        fprintf(stderr, "Thread creation failed.\n");
        return 1;
    }

    static MTAdd_server mtadd_server;
    if(!server.registry()->register_obj(&mtadd_server, "mtadd_server").is_valid())
    {
        printf("Could not register 'mtadd_server' service.\n");
        return 1;
    }

    printf("Welcome to the 'mtadd_server' multi-threaded server\n");
    server.loop();
    return 0;
}
