from TTS.api import TTS

file1 = open("Medical biology.txt")
file2 = open("Medical chemistry.txt")

txt1 = file1.read()
txt2 = file2.read()

file1.close()
file2.close()

replacement_map1 = {
    'mRNA' : 'em ar en ay',
    'ncRNA' : 'en see ar en ay',
    'miRNA' : 'my ar en ay',
    'cRNA' : 'see ar en ay',
    'tRNA' : 'tee ar en ay',
    'rRNA' : 'ar ar en ay',
    'dNTP' : 'dee en tee pee',
    'NAD+' : 'en ay dee plus',
    'NADH' : 'en ay dee aech',
    'ADP' : 'ay dee pee',
    'FAD' : 'eff ay dee',
    'GTP' : 'gee tee pee',
    'GPCRs' : 'gee pee see ars',
    'cAMP' : 'see ay em pee',
    'α'  : 'alpha',
    'γ'  : 'gamma',
    'β'  : 'beta',
    'δ'  : 'delta',
    'μ'  : 'micro',
    'π'  : 'pie',
    '5’'  : 'five prime',
    '3’'  : 'three prime',
    "5'"  : 'five prime',
    "3'" : 'three prime',
    '5′'  : 'five prime',
    '3′'  : 'three prime',
    '='  : 'equals',
    '–'  : '-',
    '°'  : ' degrees ',
    '^circ'  : ' degrees ',
    '℃'  : ' degrees celcius ',
    '/'  : ' slash ',
    '”'  : '"',
    '“'  : '"',
    '∆'  : 'delta',
    '→'  : ' gives rise to ',
    '%'  : ' percent ',
    'ø'  : 'o',
}
replacement_map2 = {
    'DNA'  : 'dee en ay',
    'RNA'  : 'ar en ay',
    'NTP'  : 'en tee pee',
    'ATP'  : 'ay tee pee',
    'AMP' : 'ay em pee',
    '×'  : ' times ',
    '’'  : "'",
    '+'  : ' divided by ',
    '−'  : ' minus ',
}
# model_name = TTS.list_models()[0]
# Init TTS
model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
tts = TTS(model_name)
for key in replacement_map1.keys():
    txt1 = txt1.replace(key, replacement_map1[key])
    txt2 = txt2.replace(key, replacement_map1[key])
for key in replacement_map2.keys():
    txt1 = txt1.replace(key, replacement_map2[key])
    txt2 = txt2.replace(key, replacement_map2[key])


N = 50
txt1_list = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), txt1.split('\n'))))
txt1_chunks = [txt1_list[n:n+N] for n in range(0, len(txt1_list), N)]

txt2_list = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), txt2.split('\n'))))
txt2_chunks = [txt2_list[n:n+N] for n in range(0, len(txt2_list), N)]

[tts.tts_to_file(text='\n'.join(txt), file_path=f"Medical_chemistry_p{str(i).zfill(2)}.wav") for i, txt in list(enumerate(txt2_chunks))[5:]]
[tts.tts_to_file(text='\n'.join(txt), file_path=f"Medical_biology_p{str(i).zfill(2)}.wav")   for i, txt in list(enumerate(txt1_chunks))]

# tts.tts_to_file(text=txt1,
#                 file_path="Medical biology.wav")sudo