import csv                              # csv 객체 호출

seoung_nam_data = [ ]                   # 기본 변수명 선언
header = [ ]
rownum = 0

with open("korea_floating_population_data.csv", "r", encoding = "cp949") as p_file: # 불러들일 데이터를 선언함, 한글 처리를 위한 c'p949'
    csv_data = csv.reader(p_file)       # csv 객체를 이용해 csv_data 읽기, 특별히 데이터를 나누는 기준을 정하지지 않음
    for row in csv_data:                # 읽어 온 데이터를 한 줄씩 처리
        if rownum == 0:
            header = row                # 첫 번째 줄은 데이터 필드로 따로 저장
        location = row[7]               # '행정구역' 필드 데이터 추출, 한글 처리로 유니코드 데이터를 cp949로 변환
        if location.find(u"성남시")!=-1:
            seoung_nam_data.append(row) # ”행정구역” 데이터에 성남시가 들어가 있으면 seoung_nam_data List에 추가
        rownum +=1

with open("seoung_nam_floating_population_data.csv", "w", encoding="cp949") as s_p_file:
    writer = csv.writer(s_p_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL) # csv.writer를 사용해 csv 파일 만들기 delimiter 필드 구분자, quotechar는 필드 각 데이터를 묶는 문자, quoting은 묶는 범위
    print(header)
    writer.writerow(header)             # 제목 필드 파일에 쓰기
    for row in seoung_nam_data:
        print(row)
        writer.writerow(row)            # seoung_nam_data에 있는 정보를 리스트에 쓰기