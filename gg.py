from amcp_pylib.core import Client
from amcp_pylib.module.template import CG_ADD

client = Client()
print(client.connect('172.18.191.15'))
with open('text.txt', 'r') as fin:
    text = fin.readline().strip()
    print(text)
    ans = client.send(CG_ADD(video_channel=1,
                      cg_layer=1, template='TITLE3',
                      play_on_load=1,
                      data=text))

    print(ans)
print(client)
