etc = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/실습/Data폴더/사고유형 기타.csv')
etc

etc = etc.drop(columns= ['Unnamed: 0', '2'])
etc

etc['0'] = '기타_사고건수', '기타_사망자수', '기타_부상자수'
etc

cross

road

side

edge

etc

action = pd.merge(cross, road, left_index = True, right_index=True)
action

action = pd.merge(action,side, left_index = True, right_index=True)
action

action = pd.merge(action, edge, left_index = True, right_index=True)
action

action = pd.merge(action, etc, left_index = True, right_index=True)
action