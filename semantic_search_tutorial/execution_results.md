# Semantic Search Tutorial 실행 결과

## 1단계: Document 객체 이해하기

문서 1:
  내용: Dogs are great companions, known for their loyalty and friendliness.
  메타데이터: {'source': 'mammal-pets-doc'}

문서 2:
  내용: Cats are independent pets that often enjoy their own space.
  메타데이터: {'source': 'mammal-pets-doc'}

## 2단계: PDF 문서 로드

로드된 문서 수: 106
첫 번째 페이지 내용 (앞 200자): FORM 10-KFORM 10-K
첫 번째 페이지 메타데이터: {'producer': 'Wdesk Fidelity Content Translations Version 008.001.016', 'creator': 'Workiva', 'creationdate': '2023-07-20T22:09:22+00:00', 'author': 'anonymous', 'moddate': '2023-07-26T15:13:52+08:00', 'title': 'Nike 2023 Proxy', 'source': 'example_data/nke-10k-2023.pdf', 'total_pages': 106, 'page': 0, 'page_label': '1'}

## 3단계: 텍스트 분할

원본 문서 수: 106
분할 후 청크 수: 501
첫 번째 청크 길이: 18자
첫 번째 청크 메타데이터: {'producer': 'Wdesk Fidelity Content Translations Version 008.001.016', 'creator': 'Workiva', 'creationdate': '2023-07-20T22:09:22+00:00', 'author': 'anonymous', 'moddate': '2023-07-26T15:13:52+08:00', 'title': 'Nike 2023 Proxy', 'source': 'example_data/nke-10k-2023.pdf', 'total_pages': 106, 'page': 0, 'page_label': '1', 'start_index': 0}

## 4단계: 임베딩 모델 초기화

임베딩 모델: text-embedding-3-large
샘플 텍스트: LangChain is a framework for building LLM applications.
벡터 차원: 3072
벡터 앞 5개 값: [-0.04382012411952019, -0.0007473950390703976, -0.039039745926856995, 0.014591953717172146, -0.02463959902524948]

## 5단계: 벡터 저장소 생성

벡터 저장소에 추가된 문서 수: 501

## 6단계: 유사도 검색

### 쿼리: How many distribution centers does Nike have?

검색 결과 수: 4

--- 결과 1 ---
내용: our Greater China geography, occupied by employees focused on implementing our wholesale, NIKE Direct and merchandising strategies in the region, among other functions. **In the United States, NIKE has eight significant distribution centers.** Five are located in or near Memphis, Tennessee, two of which are owned and three of which are leased. Two other distribution centers, one located in Indianapolis, Indiana and one located in Dayton, Tennessee, are leased and operated by third-party logistics providers. One distribution center for Converse is located in Ontario, California, which is leased. NIKE has a number of distribution facilities outside the United States, some of which are leased and operated by third-party logistics providers. The most significant distribution facilities outside the United States are located in Laakdal, Belgium; Taicang, China; Tomisato, Japan and Icheon, Korea, all of which we own.

--- 결과 2 ---
내용: in the United States: U.S. RETAIL STORES NUMBER NIKE Brand factory stores 213 NIKE Brand in-line stores (including employee-only stores) 74 Converse stores (including factory stores) 82 TOTAL 369 **In the United States, NIKE has eight significant distribution centers.** Refer to Item 2. Properties for further information. NIKE, INC. 2

--- 결과 3 ---
내용: direct to consumer businesses operate the following number of retail stores outside the United States: NON-U.S. RETAIL STORES NUMBER NIKE Brand factory stores 560 NIKE Brand in-line stores (including employee-only stores) 49 Converse stores (including factory stores) 54 TOTAL 663 SIGNIFICANT CUSTOMER No customer accounted for 10% or more of our consolidated net Revenues during fiscal 2023. PRODUCT RESEARCH, DESIGN AND DEVELOPMENT We believe our research, design and development efforts are key factors in our success. Technical innovation in the design and manufacturing process of footwear, apparel and athletic equipment receives continued emphasis as we strive to produce products that help to enhance athletic performance, reduce injury and maximize comfort, while decreasing our environmental impact. In addition to our own staff of specialists in the areas of biomechanics, chemistry, exercise physiology, engineering, digital

--- 결과 4 ---
내용: INTERNATIONAL MARKETS For fiscal 2023, non-U.S. NIKE Brand and Converse sales accounted for approximately 57% of total revenues, compared to 60% and 61% for fiscal 2022 and fiscal 2021, respectively. We sell our products to retail accounts through our own NIKE Direct operations and through a mix of independent distributors, licensees and sales representatives around the world. We sell to thousands of retail accounts and ship products from **67 distribution centers outside of the United States**. Refer to Item 2. Properties for further information on distribution facilities outside of the United States. During fiscal 2023, NIKE's three largest customers outside of the United States accounted for approximately 14% of total non-U.S. sales. In addition to NIKE-owned and Converse-owned digital commerce platforms in over 40 countries, our NIKE Direct and Converse direct to consumer businesses operate the following number of retail stores outside the United States:

### 쿼리: What was Nike's revenue? (점수 포함)

결과 1: 점수=0.6194
  내용: YEAR ENDED MAY 31, (Dollars in millions) 2023 2022 2021 REVENUES North America  &dollar;21,608 &dollar;18,353 &dollar;17,179 Europe, Middle East & Africa 13,418 12,479 11,456 Greater China 7,248 7,547 8,290 Asia Pacific & Latin America 6,431 5,955 5,343 Global Brand Divisions 58 102 25 Total NIKE Brand 48,763 44,436 42,293 Converse 2,427 2,346 2,205 Corporate 27 (72) 40 **TOTAL NIKE, INC. REVENUES &dollar;51,217** &dollar;46,710 &dollar;44,538 EARNINGS BEFORE INTEREST AND TAXES North America &dollar;5,454 &dollar;5,114 &dollar;5,089 Europe, Middle East & Africa 3,531 3,293 2,435 Greater China 2,283 2,365 3,243 Asia Pacific & Latin America 1,932 1,896 1,530 Global Brand Divisions (4,841) (4,262) (3,656) Converse 676 669 543 Corporate (2,840) (2,219) (2,261) Interest expense (income), net (6) 205 262 TOTAL NIKE, INC. INCOME BEFORE INCOME TAXES &dollar;6,201 &dollar;6,651 &dollar;6,661 ADDITIONS TO PROPERTY, PLANT AND EQUIPMENT North America &dollar;283 &dollar;146 &dollar;98 Europe, Middle East & Africa 215 197 153

결과 2: 점수=0.6158
  내용: NIKE, INC. CONSOLIDATED STATEMENTS OF INCOME YEAR ENDED MAY 31, (In millions, except per share data) 2023 2022 2021 <b>Revenues &dollar;51,217</b> &dollar;46,710 &dollar;44,538 Cost of sales 28,925 25,231 24,576 Gross profit 22,292 21,479 19,962 Demand creation expense 4,060 3,850 3,114 Operating overhead expense 12,317 10,954 9,911 Total selling and administrative expense 16,377 14,804 13,025 Interest expense (income), net (6) 205 262 Other (income) expense, net (280) (181) 14 Income before income taxes 6,201 6,651 6,661 Income tax expense 1,131 605 934 NET INCOME &dollar;5,070 &dollar;6,046 &dollar;5,727 Earnings per common share: Basic &dollar;3.27 &dollar;3.83 &dollar;3.64 Diluted &dollar;3.23 &dollar;3.75 &dollar;3.56

결과 3: 점수=0.6150
  내용: FISCAL 2023 NIKE BRAND REVENUE HIGHLIGHTS The following tables present NIKE Brand revenues disaggregated by reportable operating segment, distribution channel and major product line: FISCAL 2023 COMPARED TO FISCAL 2022 **NIKE, Inc. Revenues were &dollar;51.2 billion in fiscal 2023, which increased 10%** and 16% compared to fiscal 2022 on a reported and currency-neutral basis, respectively. The increase was due to higher revenues in North America, Europe, Middle East & Africa ("EMEA"), APLA and Greater China, which contributed approximately 7, 6, 2 and 1 percentage points to NIKE, Inc. Revenues, respectively.

결과 4: 점수=0.6043
  내용: apparel revenue growth. Higher ASP was primarily due to higher full-price ASP and growth in the size of our NIKE Direct business, partially offset by lower NIKE Direct ASP, reflecting higher promotional activity. **NIKE Direct revenues increased 14% from &dollar;18.7 billion in fiscal 2022 to &dollar;21.3 billion in fiscal 2023.** On a currency-neutral basis, NIKE Direct revenues increased 20% primarily driven by NIKE Brand Digital sales growth of 24%, comparable store sales growth of 14% and the addition of new stores.

## 7단계: 리트리버 사용

### 단일 쿼리: When was Nike incorporated? (k=1)

쿼리: When was Nike incorporated?
검색 결과 수: 1
내용: NIKE, INC. One Bowerman Drive Beaverton, OR 97005-6453 www.nike.com

> 정답인 "incorporated in 1967"은 이 청크에 포함되어 있지 않음

### 배치 쿼리

쿼리: How many distribution centers does Nike have?
  결과: our Greater China geography, occupied by employees focused on implementing our wholesale, NIKE Direct and merchandising strategies in the region, among other functions. **In the United States, NIKE has eight significant distribution centers.** Five are located in or near Memphis, Tennessee, two of which are owned and three of which are leased. Two other distribution centers, one located in Indianapolis, Indiana and one located in Dayton, Tennessee, are leased and operated by third-party logistics providers. One distribution center for Converse is located in Ontario, California, which is leased. NIKE has a number of distribution facilities outside the United States, some of which are leased and operated by third-party logistics providers. The most significant distribution facilities outside the United States are located in Laakdal, Belgium; Taicang, China; Tomisato, Japan and Icheon, Korea, all of which we own.

쿼리: What was Nike's revenue?
  결과: YEAR ENDED MAY 31, (Dollars in millions) 2023 2022 2021 REVENUES North America U+002421,608 /U+0024/18,353 &dollar;17,179 Europe, Middle East & Africa 13,418 12,479 11,456 Greater China 7,248 7,547 8,290 Asia Pacific & Latin America 6,431 5,955 5,343 Global Brand Divisions 58 102 25 Total NIKE Brand 48,763 44,436 42,293 Converse 2,427 2,346 2,205 Corporate 27 (72) 40 **TOTAL NIKE, INC. REVENUES &dollar;51,217** &dollar;46,710 &dollar;44,538 EARNINGS BEFORE INTEREST AND TAXES North America &dollar;5,454 &dollar;5,114 &dollar;5,089 Europe, Middle East & Africa 3,531 3,293 2,435 Greater China 2,283 2,365 3,243 Asia Pacific & Latin America 1,932 1,896 1,530 Global Brand Divisions (4,841) (4,262) (3,656) Converse 676 669 543 Corporate (2,840) (2,219) (2,261) Interest expense (income), net (6) 205 262 TOTAL NIKE, INC. INCOME BEFORE INCOME TAXES &dollar;6,201 &dollar;6,651 &dollar;6,661 ADDITIONS TO PROPERTY, PLANT AND EQUIPMENT North America &dollar;283 &dollar;146 &dollar;98 Europe, Middle East & Africa 215 197 153
