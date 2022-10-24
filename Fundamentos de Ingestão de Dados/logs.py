#%%import backoff
import random
import logging
import backoff

#%%
#salvando o logs utilizando o logging
log = logging.getLogger()
log.setLevel(logging.DEBUG) #define o nivel do log
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
channel = logging.StreamHandler()
channel.setFormatter(formatter)
log.addHandler(channel)


# %%
#Simulando a API e usando o backoff
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
   
    rnd = random.randint(100, 1000)
    log.debug(f"RND: {rnd}")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
   
    if rnd < 200:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
        
    elif rnd < 400:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < 600:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    
    else:
        return "OK!"

# %%
test_func()
# %%
