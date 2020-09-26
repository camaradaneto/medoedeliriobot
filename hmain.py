import tweepy
import random
import time
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

max_tweets = 20

list_delirio = ['paralepíp de crack', 'terrívelmente evangélico', 'golden shower',
                'isso comprova a confiança do mundo em nosso governo',
                'os livros hoje em dia, como regra, são um montão de amontoado de muita coisa escrita']

list_isso = ['é uma CANALHICE isso que vcs fazem!',
             'meu histórico de atleta!', 'uma gripezinha!\n um resfriadinho!', 'putinha do bozo',
             'fase terminal do aparelho digestivo']

list_acabou = ['acabou porra!', 'então bundão é o Jair!',
               'eu sou louco? não!\n eu tô louco? não!\n eu não sou louco!\n eu não sou louco!']

delirio = random.choice(list_delirio)
isso = random.choice(list_isso)
acabou = random.choice(list_acabou)


def get_id():
    with open('ultimoid.txt', 'r') as f:
        ultimoid = f.read()
    return ultimoid


def salva_id(novo_ultimo_id):
    with open('ultimoid.txt', 'w') as f:
        f.write(str(novo_ultimo_id))


def responde():
    ultimoid = get_id()
    ids_pegos = []
    try:
        for tweet in tweepy.Cursor(api.mentions_timeline, since_id=ultimoid).items(max_tweets):
            ids_pegos.append(tweet.id)
            user_name = tweet.user.name
            status = api.get_status(tweet.id)
            if 'frota' in status.text.lower():
                api.update_status('@' + user_name + '\n ator pornô', in_reply_to_status_id=tweet.id)
            elif 'ator pornô' in status.text.lower():
                api.update_status('@' + user_name + '\n porra merval', in_reply_to_status_id=tweet.id)
            elif 'delírio' in status.text.lower():
                api.update_status('@' + user_name + '\n' + delirio, in_reply_to_status_id=tweet.id)
            elif 'é isso?' in status.text.lower():
                api.update_status('@' + user_name + '\n' + isso, in_reply_to_status_id=tweet.id)
                time.sleep(6)
            else:
                api.update_status('@' + user_name + '\n' + acabou, in_reply_to_status_id=tweet.id)
                time.sleep(6)
        salva_id(max(ids_pegos))
    except Exception:
        pass


if __name__ == '__main__':
    responde()
