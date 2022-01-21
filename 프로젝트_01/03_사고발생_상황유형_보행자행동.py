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

action.columns

action.loc[0]

action = action.drop(columns=['0_x', '0_y', '0'])
action

action.columns = ['횡단중', '차도통행중', '보도통행중', '길가장자리통행중', '기타']

action.index = ['사고발생건수', '사망자수', '부상자수']
action

#action

action_a = action.columns

action = action.T
action

action = action.reset_index()
action

action.columns=['행동유형', '사고발생건수', '사망자수', '부상자수']
action

a_type = action['행동유형'].values.tolist()

a_type

num = action['사고발생건수'].values.tolist()
num

death = action['사망자수'].values.tolist()
death

injury = action['부상자수'].values.tolist()
injury