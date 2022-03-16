import requests
import re
from tqdm import tqdm  # 进度条

url = 'https://vd.l.qq.com/proxyhttp'
headers = {
    'cookie': 'RK=GDLQtsCqEP; ptcz=e598de8d32a48d8b2a036b763604b34d0e5d41bbc0bc89adf37ca075e51264c7; tvfe_boss_uuid=2f54e3d09274069c; pgv_pvid=2230046660; o_cookie=562172420; o_minduid=OOUNFmj_2gbebzluxba3jOfcs3TWpu0-; appuser=CEBAF9E84D8714DA; pac_uid=1_562172420; eas_sid=t156Y4O0H0t9C0R3O0t0t0M8m3; luin=o0562172420; fqm_pvqid=36260b0a-2a8a-488c-b5ec-04ded58eb627; lskey=00010000407213dfe78ad62fb62360a0226641c3a0645562a3b4a9108f5ad5696711043da25c9e0bcc95d697; video_omgid=744c858379718e45; vversion_name=8.2.95; pgv_info=ssid=s850541216; LCZCturn=983; Lturn=95; LKBturn=138; LPVLturn=635; LPLFturn=732; LPSJturn=8; LBSturn=991; LZCturn=811; LVINturn=535; LPHLSturn=431; LPCZCturn=392; LPPBturn=990; LPDFturn=991; LZTturn=148',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
data = {
    'adparam': 'pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200mp8vo9b%2Fn0041aa087e.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=mzc00200mp8vo9b&vid=n0041aa087e&pt=&flowid=584292bdeced4e3c936cb574f20a3154_10201&vptag=%7Cx&pu=1&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=a847f66dc6d04dd47f08d7baceea28d1&req_type=1&from=0&appversion=1.0.173&lt=qq&platform=10201&tpid=2&rfid=e47517b30484d4f89ed9837cf584360d_1642313606',
    'buid': 'vinfoad',
    'vinfoparam': 'spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=a847f66dc6d04dd47f08d7baceea28d1&flowid=584292bdeced4e3c936cb574f20a3154_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200mp8vo9b%2Fn0041aa087e.html&refer=v.qq.com&sphttps=1&tm=1642924739&spwm=4&logintoken=&vid=n0041aa087e&defn=shd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=1&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=G3XaeOkqlmJ6JZEItZs_lpJX5WB4a2CdS8kErtWYVaqtHEZQ1c_W6myJ8hQDnmDFHJF-S53MPzvp2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op8F_DerfPItxgg_6KY-qnwqEERQEIvYluNDEH6IC8EOljLQ2VfW2sTdospNPlD9535CNT9iSo3cLRH93ogtX_OJeYNVWrDYS8b5t1pjAAuGkoYGNScB_8lMah6WVCJtO-Ygxs9f-BtA8Y-UT7SJi2_VH7z0s2I0jf9_AUNIsHEG9zgzglpES47qAUrvH-0706f5Jz35DBkQKl4XAh32cbyy4fOERC431b3NsHmFzmlL2RlhboG4clInAcKtD_-mNNOrTjlxuBcWYMGUyy9HW_YGBgYGBgZPUl7z&fp2p=1&spadseg=3',
}
response = requests.post(url=url, json=data, headers=headers).json()
vinfo = response['vinfo']
# print(vinfo)
m3u8_url = re.findall('url":"(.*?)"', vinfo)[3]
# print(m3u8_url)
m3u8_data = requests.get(url=m3u8_url).text
m3u8_data = re.sub('#EXT.*', '', m3u8_data).split()
# print(m3u8_data)
for value in tqdm(m3u8_data):
    moive = 'https://apd-1d138d1170ca26ec08f3b992dd949c49.v.smtcdns.com/moviets.tc.qq.com/AXnCkmAD3pRLZ03XcIisvAvtTroimyZt9ilvYbtk2C84/uwMROfz2r57AoaQXGdGnC2de64-aQGMBaghPzSlG8CDdub8-/svp_50112/0R0BJ97MvX5JtYJ130yYYrnmp8DMj7gGWprA_BnA3VIYQJ04VDhG2Mwn-gCEgwRRkOhcKCmNLiUvXwrp1ce674GitkIOHGaOgIN565CLo3gUIJMtNls_Z74pQ4pk-xQvXOOVLOE_2tu7ibbr-pRBus3YuHrM86rWY54r3vPe0CdwxiHCyrpv_A/'
    moive_url = moive + value
    moive_content = requests.get(url=moive_url).content
    with open('开端1.mp4', mode='ab') as f:
        f.write(moive_content)
print('over')
