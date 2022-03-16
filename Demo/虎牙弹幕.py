import requests
import re
import csv

f = open('弹幕.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['Name', 'Text', 'Time'])
csv_writer.writeheader()
url = 'https://v.huya.com/cat/51'
headers = {
    'cookie': 'huya_ua=webh5&0.0.1&websocket; udb_guiddata=59da5dc239084284b4b6eb8ab33ff102; udb_deviceid=w_509432920016977920; __yamid_tt1=0.20640548667961434; __yamid_new=C995D7A35820000122CF179F56101CD5; game_did=KTLeSqJ1JzfBFserXkPDXt7VObaJtyWrWff; alphaValue=0.80; SoundValue=1.00; videoBitRate=0; videoLine=5; isInLiveRoom=; udb_passdata=3; __yasmid=0.20640548667961434; huya_web_rep_cnt=50; huya_ua=webh5&0.0.1&websocket; guid=0a70a96f9b9f18627401ce77cf773e59; udb_biztoken=AQA_k8OP14tz68a7TuvwmD68E_ms7PFefOuF-b6x6P-yq9AI_orN-OcMtDWlucF633uTIO0SP29auUBtUFhK1-dmSWv6k7yQQ1Qt0OV6UTNuEsoVz8fR8NOo3vcAp2fY7vss4lVH_TQwHVoqhO8IfbFmhq6pxp6D9v2_lB3IHQpEZE_vvLyqFnpdSmYRrGRiFhYiHBFMeokpORBqqLhUMMEu6j1Vq9lR-0FXglPExKKLaddl18NA-not7NJqoqVN6AmHpe-KchdtYBD2bJHitKWu4Spc-IF7SwRr-rVl-FYHmwS_PEK8f6qYJ1E6waPKb3uIIg5bBUe8I08qwNxWacCR; udb_cred=CnBh89_Ce7A5grWJ270FHuUiytbmbSiumY9sISNZHKVTKRTPKR-aL71cRQVHm6Jw-mAdPc-Bw9g8BE-V0z5xC2dKFCmCRCRXSyiV2bxj6jHde3Vhy8d6CBXs3WE-xkUHGjk; udb_origin=1; udb_other=%7B%22lt%22%3A%221645780919944%22%2C%22isRem%22%3A%221%22%7D; udb_passport=hy_145332481; udb_status=1; udb_uid=1199575991840; udb_version=1.0; username=hy_145332481; yyuid=1199575991840; udb_accdata=08618533538210; __yaoldyyuid=1199575991840; _yasids=__rootsid%3DC9B98E2CDB600001897E1D3110EA1DED; PHPSESSID=3noca50q188sjvn8m5303j1j11; h_unt=1645780959; hiido_ui=0.36880279692568685; amkit3-v-player-profile-volume=0.13902394364519818; amkit3-v-player-profile-definition=yuanhua; amkit3-player-danmu-pop=1; rep_cnt=68',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36,'
}
response = requests.get(url, headers=headers).text
videoId = re.findall('"vid":(\d+),"liveId"', response)
i = 0
for id_ in videoId:
    id_url = f'https://cxt.huya.com/open/danmu/list.do?vid={id_}'
    res = requests.get(id_url, headers=headers).json()
    for comment in res:
        Name = comment['nick']
        Text = comment['text']
        Time = comment['submitTime']
        data_dict = {
            'Name': Name,
            'Text': Text,
            'Time': Time,
        }
        print(data_dict)
        csv_writer.writerow(data_dict)
    i += 1
    print(i)

print('over')
