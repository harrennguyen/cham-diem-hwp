import streamlit as st
import difflib
import re

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hệ thống chấm điểm gõ tiếng Hàn", layout="wide")

# ==============================================================================
# 📋 KHU VỰC CẬP NHẬT 25 BÀI VĂN BẢN GỐC CỦA THẦY
# Thầy chỉ cần thêm/sửa tên bài và nội dung chữ tiếng Hàn ở đây theo đúng cấu trúc:
# "Tên bài": """Nội dung bài gõ""",
# ==============================================================================
DANH_SACH_BAI_MAU = {
    "15살부터 64살까지를 생산 가능 인구": 
        """개요
        15살부터 64살까지를 생산 가능 인구(Productive Age)로 봤을 때 이들이 65살 이상 노인을 부양(扶養)하는 비율, 즉 노인부양비는 올해 11.6%에서 2020년에는 21.3%, 2030년에는 35.7%, 2050년에는 62.5%로 늘어날 것으로 전망된다. 거칠게 말하면 현재는 9명이 한 명의 노인을 부양하지만 2050년에는 1.6명이 한 명의 노인을 부양해야 한다. 이러한 시점에서 고갈되고 있는 국민연금(National Pension)의 재정(Finance) 안정화를 위한 방안(Plan)이 국회에 상정되었으나 국회(Congress) 통과는 힘들 것으로 보인다. 채권 유통 물량이 적으면 채권 펀드(Fund)가 수익(Revenue)을 올리기가 쉽지 않아진다. 의도(意圖)하지 않은 이런 현상은 재정 안정화 대책(Counterplan)이 채택돼 국민연금 기금의 증가세에 가속이 붙으면 더 빈번하게 출현할 수 있다.

        자산(Assets) 편식 심각
        국민연금은 채권(Bond) 편식가이다. 한국개발연구원(Korea Development Institute)의 자료(Data)에 따르면, 2015년 국민연금 기금의 금융(金融) 부분 투자 비중에서 채권은 91%를 차지했다. 금융자산 중 주식은 5%였다.
        국민연금이 발행 국공채(Government Bond) 물량을 대거 흡수하면서 시장 유통 물량이 줄어 채권 가격(Price)이 잘 형성되지 않고 있다고 불만(Dissatisfaction)을 털어놓는다.

        개선 대책 필요성
        국민연금의 고갈(Exhaustion)에 대한 우려(憂慮)의 목소리가 높아지고 있다. 더 내고 덜 받아도 다음 세대(Generation)를 생각하라며 희생(Sacrifice)을 강요하기도 한다.
        먼저 우리 앞에 나타난 해법(Solution)은 재정 안정화 대책이다. 구조의 개선(Reformation)이라는 해법은 아직 현실화되지 못한 상태다.

        눈앞에 있으나 미흡한 해법을 택할 것인가. 근본적이나 멀리 있는 해법을 찾아 돌아갈 것인가. 정부뿐만 아니라 국민이 신중히 생각해야 할 문제다.

        참고문헌
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Wiliam. K. Narayan(2010). The Autobiography Urinalysis of the way to Samurai, Easy Press. pp56-89.
        Jerry Vanzant(2012). The Emergence of Puddiing Away, ABC Press. pp13-25.""",
        
    "2010년까지 산업은": 
        """개요
        2010년까지 산업은 그야말로 초고속성장을 보여 주었다. 2011년 유럽의 재정위기로 인하여 유럽 시장이 붕괴될 것이라는 전망이 태양광 시장의 암울한 미래를 예언하였다. 하지만 2011년 실제 상황은 달랐다. 유럽(Europe)의 시장이 축소된 만큼 미국(USA), 중국(China) 시장이 크게 성장하면서 2011년에도 2010년 대비 76% 이상 성장하며 2011년 한 해에만 29.5 GW를 설치하였으며, 2012년에도 28.4 GW를 설치하여 2011년 정도의 시장규모를 유지하였다. 
        2013년의 경우 태양광(Solar Energy) 시장은 다시 성장하며 최소 39 GW의 규모를 형성한 것으로 조사되었다. 2013년 말 기준 세계 태양광 시장의 누적 설치량은 140 GW 이상이다.

        세계 태양광 시장 현황 분석
        2013년 태양광 시장은 2012년에 비해 35% 이상 크게 성장하였다.
        유럽 시장의 비중(比重)은 2011년 75%에서 2013년 28%로 크게 줄어든 반면에 아시아/태평양 시장은 2011년 17%에서 2013년 57%로 크게 성장하고 있다.
        2011년과 2012년에는 독일과 이탈리아 시장이 가장 큰 규모이었지만 2013년은 중국, 미국의 순으로 시장 규모의 순위가 바뀌었다.
        태양광 시장의 변화로 독립형 시스템의 비중은 크게 하락하였고 대부분의 시장이 계통 연계형 시스템으로 전환(轉換)되었다.

        태양광 지원정책 조사
        IEA PVPS 참여국을 대상으로 조사한 결과 FIT 제도가 70%로 압도적으로 많았다. 우리나라가 채택하고 있는 RPS 정책(政策)의 경우 3% 정도 밖에 되지 않는다. 우리나라의 태양광 설치량은 2008년 276 MW를 정점으로 지속적으로 하락하여 2011년 156 MW 규모로 축소되었다.
        RPS 제도의 도입으로 2012년 시장은 다시 크게 성장하며 2012년 230 MW, 2013년 531 MW의 시장 규모를 형성하였으며, 2013년 기준 누적 설치량도 1,555 MW로 우리나라도 GW 규모의 국가가 되었다. 연간 성장률은 크게 퇴조하였다. 특별한 이슈 없이는 당분간 이러한 추세는 계속될 전망이다.

        참고문헌
        Guillen, M.(2008). Building a Global Bank, Princeton University Press. pp34-45.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.

        시나공 기자(abc@sinagong.co.kr)""",
        
    "2015년 2월 발표(發表)된": 
        """개요
        2015년 2월 발표(發表)된 인간지놈프로젝트(Human Genome Project)의 결과는 생명 현상의 이해와 각종 질병치료의 혁신에 새로운 장을 연 것으로 평가된다. 그러나 전문가들은 1차원적인 염기서열과 지도만으로 지놈프로젝트에 거는 기대를 충족시키기에는 부족하다고 말하며 지놈의 기능 해석이 뒤따라야만 한다고 입을 모은다. 지놈 수준에서부터 실제 생명현상을 일으키는 단백질의 영역에 이르는 정보(Information)와 지식(Knowledge)의 통합이 이루어지는 이른바 포스트지놈 시대의 중요성을 강조하고 있는 것이다.

        프로티오믹스 관련 정보
        지놈에서 만들어지는 단백질의 총체인 프로티옴(Proteome)을 다루는 분야를 프로티오믹스라 한다.
        프로티오믹스는 당초 정상적인 세포와 그렇지 않은 세포의 단백질들을 분리, 비교 분석하는 의미로 사용되었으나 현재는 기능 지노믹스, 구조 프로티오믹스, 단백질간 상호작용, 생화학대사 경로의 연구(硏究)까지를 총망라하는 개념으로 발전하였다.
        지놈에서 나오는 단백질들의 구조, 기능, 상호작용 등을 밝히는 프로티오믹스(Proteomics)가 지놈의 구조 및 기능을 밝히는 지노믹스(Genomics)와 함께 이러한 필요를 충족시켜 줄 수 있는 분야로 주목을 받고 있다.

        관련 시장의 분류
        프로티오믹스 분석(分析)을 위한 기기 및 관련 기술을 제공하는 분야는 전통적인 프로티오믹스를 위한 2-DE(2-Dimensional Gel Electrophoresis)/MS(Mass Spectrometry)에 필요한 분석기기와 기술을 제공하는 분야이며 AP Biotech, Bio-Rad, Applied Biosystems, Waters 등이 대표적인 기업들이다.
        프로티오믹스 서비스를 제공하는 분야는 전체 프로티오믹스 시장의 20%가량을 차지하고 있으며, 대표적인 기업(企業)들로는 Oxford GlycoSciences, MDS Protana 등을 들 수 있는데 이들은 2-DE/MS 등의 분석 기술을 보유하고 있으며 제약기업과의 공동연구를 통해 프로티오믹스 분석 서비스를 제공하고 있다.

        참고문헌
        Wiliam. K. Narayan(2010). The Autobiography Urinalysis of the way to Samurai, Easy Press. pp56-89.
        Jerry Vanzant(2012). The Emergence of Puddiing Away, ABC Press. pp13-25.
        Guillen, M.(2008). Building a Global Bank, Princeton University Press. pp34-45.""",
        
    "2017년 들어 미국경제의 주요": 
        """2017년 들어 미국경제의 주요 지표들이 서로 상반되는 방향으로 나타나 경기전망을 엇갈리게 하고 있다. 그러나 대체적인 예측(豫測)은 미국의 경제성장률(Rate of Economic Growth)이 하락하고 있는 것으로 나타나고 있다.

        미국의 경기 둔화
        지난해 4/4분기의 경제성장률은 1.1%로 예상치인 1.4%보다 더 하락한 것으로 나타났다. 이는 지난해 3/4분기의 2.2%, 상반기 5% 이상의 성장에서 매우 크게 하락한 것이며, 15년 2/4분기의 0.8% 성장 이후 가장 낮은 성장률을 나타낸다.
        올해 1/4분기에는 제로에 가까운 경제성장률을 보일 것이라는 예측이다. 또한 컨퍼런스 보드(Conference Board)가 조사한 소비자신뢰지수(Consumer Confidence Index)는 5개월 연속 하락해 향후 경기둔화가 계속 이어질 것임을 시사하고 있다. 이는 1월 114.4%, 지난해 12월의 128.6%에 비해 크게 하락한 것이다.

        소비자신뢰지수와는 반대로 미국의 제조업지수, 개인소득, 소비는 소폭 증가한 것으로 나타났다. 전미구매관리협회(NAPM : National Association of Purchasing Management) 제조업생산지수는 지난 2월 41.9%를 기록(記錄)했는데 이는 10년 만에 최저치였던 1월의 41.2%에 비해 0.7% 상승한 것이다.

        경기하락의 원인
        경기가 침체하면서 시장에서는 연방공개시장위원회(FOMC : Federal Open Market Committee)가 열리는 3월 20일 이전에라도 금리가 추가로 인하될 수 있을 것이라고 기대했지만 개인소득과 소비지출이 증가한 것으로 나타나면서 금리의 조기인하는 실현되지 않았다. 물론 향후 발표되는 소매매출과 기업재고 등의 내용이 연준(Federal Reserve Board)의 결정에 영향을 미치겠지만 대부분의 전문가들은 0.5%P(Percent Point) 정도의 금리인하를 예상하고 있다.
        이와 같이 금리인하에도 불구하고 주가가 하락하는 것은 기업(企業)들의 실적악화에 기인한다. 그 예로 인터넷기업(Internet Business)의 대표 주자인 야후(Yahoo)의 실적악화 및 그에 따른 CEO 교체, 인텔(Intel)의 순익부진 전망 및 그에 따른 인원감축 계획 등은 향후 기술주에 대한 전망을 어둡게 했다.""",
                
    "ME(Micro Electronic)란": 
        """개요
        ME(Micro Electronic)란 정밀전자공학이라는 뜻으로 처음에는 집적회로(Integrated Circuit)의 제조기술을 뜻하는 것이었다. 생산현장에서는 산업용 로봇이 도입되어 자동화되었고, 유연생산체제 즉 FMS(Flexible Manufacturing System) 공장이 보급되어 무인화공장이 등장하였다. 압도적인 ME는 디지털 경제(Digital Economy)라는 용어로 통용되고 있으며 그 핵심은 Analog를 Digital로, Off-Line을 On-Line으로 변화시키는 것이라고 할 수 있다. Electronic은 이제 디지털이라는 컨텐츠의 구조를 나타내는 용어로 대치되고 있는 것이다. ME혁명(革命)은 노동과정에도 큰 혁신을 일으켰다. 정보시스템(Information System)의 혁신(革新)은 서류작업(Paper Work)을 네트워크로 대체하여 무서류작업(No Paper Work)을 가능케 하였다.

        ME가 미치는 영향 분석
        ME로 인한 노동의 변화를 위 자료에서 보면 노동시장의 구조가 정규직에서 임시 근로자로 대체되고 있음을 알 수 있다.
        ME로 인하여 고용구조가 크게 변화하여 전체 취업자 중 상용근로자의 비중이 급속히 낮아진 반면, 임시근로자의 비중은 크게 높아졌음을 알 수 있다.
        임시근로자나 시간제근로자의 비중이 상승하는 것은 고용이 불안해진다는 측면이 있다.
        공정전반에 걸친 유연생산체계(Flexible Manufacturing System)가 성립되면서 컴퓨터로 Plan, Design, 제조된 제품은 네트워크(Network)로 연결되어 사람 사이의 접촉이 차단되는 수평적 위계화가 성립된다.

        종합적 평가
        ME의 진행(進行)은 완전경쟁 시장에 근접해갈 것이라는 것이다.
        생존을 위해서는 가장 낮은 비용, 좋은 제품을 생산, 판매하는 효율성을 가진 소비자들만 존재하고, 소비자의 주권이 실현되며, 노동 공급과 수요도 완전한, 그렇기에 소비자 잉여와 생산자 잉여로 이뤄지는 사회의 후생은 여타 다른 어떠한 시장 구조보다 극대화되는 시장 구조가 될 것이라는 것이다.

        참고문헌
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.""",
    
    "Visitor의 욕구가 있고 구매력을": 
        """개요
        Visitor의 욕구가 있고 구매력을 갖춘 관광객들의 집합을 관광시장이라고 본다면 시장에 대하여 제품과 서비스를 생산 및 판매하는 조직적인 사업을 관광기업이라고 한다. 이러한 기업들을 관광산업(Tourist Industry)이라고 할 수 있다. 관광산업의 정의를 보면, 관광산업은 여행과 Recreation을 위해 전체적인 면에서 Merchandise, Communication, Service 시설과 기타 시설, 그리고 정부기관이 상호 관련된 합성체로 정의하고 있다. 관광산업의 관광객은 소비자로 오기 때문에 그들이 가지고 오는 외화는 무형적인 수출이기도 하며 관광산업의 외환수입은 국제수지(the Balance of International Payment) 개선효과와 국제무역(International Trade)을 자극한 무역진흥의 동기부여가 될 수 있다. 관광산업은 국토개발(Land Development)의 일환으로 1, 2차 산업보다 비교적 공해가 적으며 자원 절약적이다.

        관광산업 전망
        관광산업은 앞으로 10년간 연평균 5% 성장하여 정보통신 산업과 더불어 21세기 성장을 주도하는 산업으로 각광받을 것으로 예측(豫測)되고 있다.
        동아태지역은 다양한 관광자원과 전반적인 경제발전으로 관광여건이 개선되는 가운데 성장을 지속하여 관광객 수가 표에서 보듯이 2010년 5,300만 명에서 2020년 1억100만 명으로 2배 이상 성장할 것으로 보인다.
        관광산업의 시장점유율은 20%로 급상승할 것이며 특히 수송(輸送)수단이 획기적으로 개선될 것으로 기대되는 2015년 이후에는 10%대 이상의 고도성장을 지속함으로써 21세기 세계 관광시장을 주도할 것으로 예상된다.

        제안
        우리나라도 21세기에는 China, Russia로 가는 경유지로서의 역할(役割)이 부각되고 관광 형태도 유적지나 휴양지를 방문하던 단순한 패턴에서 일정기간 각종 Tourist Event에 참가하는 참여관광 형태로 바뀌면서 관광입지가 크게 호전될 것으로 보인다.
        2018년 평창 올림픽대회의 대형 International Event가 우리나라에서 개최된다는 것은 관광산업 발전을 위한 기회라 할 수 있다.

        참고문헌
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Wiliam. K. Narayan(2010). The Autobiography Urinalysis of the way to Samurai, Easy Press. pp56-89.
        Jerry Vanzant(2012). The Emergence of Puddiing Away, ABC Press. pp13-25.""",
        
    "강남강동권 아파트값(the Price of Apartment)": 
        """개요
        강남/강동권 아파트값(the Price of Apartment)이 상승세(Ascending Current)를 보이고 있다. 주간 변동폭을 보면 강남은 평균 0.2%-0.3%, 강동은 0.3%-0.4% 대의 변동률을 보였다. 서울시 평균 가격변동률보다 배 이상 높은 수치다. 재건축(Rebuilding) 시공사(the Company of Construction) 선정이 잇따르면서 가격이 치솟고 있는 두 지역은 지난주에도 강남 0.39%, 강동 0.51%의 가격상승률을 기록했다. 이에 따라 강남은 3월초 대비 6월 현재 제곱미터(m2)당 평균값 기준으로 32만 4,200원, 강동은 23만 3,700원 정도 올랐다.

        수도권 현황
        수도권(the National Capital Region)에서도 재건축 바람이 불고 있는 경기도 지역의 가격상승세(the Current of Price Advance)가 두드러졌다.
        신도시를 비롯한 변두리 지역(地域)은 0.1% 대의 적은 가격 변동률(the Range of Fluctuation in Price)을 기록했다.
        강남, 강동, 서초권은 재건축 단지를 중심으로 투자수요가 집중되고 전세부족으로 인한 소형 매매 실수요가 늘어 강세가 이어지고 있다.
        82.6(제곱미터) 이하 소형아파트는 0.48%의 상승률을 기록했고 181.8(제곱미터) 이상 대형은 Minus 0.27%로 하락세를 보였다.
        전체적으로 강남(0.39%), 강동(0.51%), 강북(0.35%), 관악(0.25%), 서초(0.31%), 송파(0.18%) 등이 높은 상승세를 나타냈다.

        상승률 분석
        오름세를 보인 아파트로는 양천구 목동 황제 56.2(제곱미터)가 재건축 사업승인과 함께 문의가 늘며 4월 마지막주 대비 1,000만원 오른 1억 850만원에 시세가 형성됐다.
        저밀도 지구에 속하는 역삼동 개나리 1차 21, 85.9(제곱미터)도 1,500만-2,000만원 올랐다. 4월 마지막 주말 DL건설로 시공사를 확정한 삼성동 홍실도 102.5(제곱미터)가 2억 9,000만원으로 지난주 대비 1,000만원 올랐다.
        강동구에서도 등촌동 청우, 둔촌동 주공 등 재건축이 거론(擧論)되고 있는 노후 단지들이 올해 들어 꾸준히 강세를 보이고 있다.

        참고문헌
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Whoopi Leibovitz(2011). The Power of Pilgrimage, GilbutSchool. pp25-29.""",
        
    "교육부(Ministry of Education)는": 
        """개요
        교육부(Ministry of Education)는 여교사 증가에 따른 학교운영실태를 파악하기 위하여, <여교사의 교단진입 증가에 따른 학교현장 실태분석>에 관한 정책 연구를 추진하였다. 연구(硏究)는 총 101개의 학교를 대상으로 교사, 학교 행정가, 학부모, 학생에 대한 설문조사와 집단면담(Group Interview)을 통해 수행되었다. 여교사 증가에 대한 부정적 견해로는 학교 운영상의 문제와 남학생의 여성화에 대한 우려 때문인 것으로 나타났다. 또한 여교사의 출산이나 육아(Upbringing of a Child)로 인한 휴가(Vacation)와 휴직(Temporary Retirement from Office)시에 대체할 강사의 수급(Supply and Demand)이 원활하지 않은 것도 원인(原因)으로 지적되었다. 그러나 여교사의 교육 활동은 우수한 것으로 나타나 여교사의 필요성이 높아지고 있다.

        연구결과
        초등학교 여교사의 비율(比率)은 2000년 40%, 2005년 47%, 2010년 52%, 2015년에는 66%에 달했다. 특히 서울, 부산, 대구 등 대도시는 70%를 상회하는 높은 수치를 보였다.
        중학교의 경우에는 2000년 35%, 2005년 42%, 2010년 48%, 2015년에는 58%로 증가했다. 중학교 여교사의 비율은 지방의 경우 57%, 대도시의 경우에는 60%의 비율을 나타냈다.
        고등학교는 2000년 18%보다 12% 증가한 30% 정도로 초, 중학교에 비해 월등히 낮은 수치였다.

        해결방안
        앞으로도 여교사의 수가 계속 늘어날 것으로 예상됨에 따라 여교사의 능력향상과 근무여건 개선(Improvement) 등 다각적인 지원책 강구가 절실하다.
        관행적으로 이루어졌던 남교사 중심의 부장 임명 방식을 개선(改選)하여, 여교사들의 업무의욕을 고취시키고 능력발휘의 기회(Opportunity)를 적극 부여하도록 할 방침이다.
        여교사들도 자질향상을 위해 스스로 노력해야겠다.

        참고문헌
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.
        Whoopi Leibovitz(2011). The Power of Pilgrimage, GilbutSchool. pp25-29.""",
        
    "우리나라 사이버 거래(Cyber Trading)": 
        """개요
        우리나라 사이버 거래(Cyber Trading) 규모는 세계 1위의 미국보다 규모(規模) 면에서는 뒤지나, 성장속도 면에서는 훨씬 빠르다. 17년 4월부터는 본격화된 사이버 증권거래가 성장속도 면에서는 한국이 미국을 앞지르고 있으며, 17년 6월 말 현재 전체 증권거래에서 사이버 거래가 차지하는 비중은 16.8%이지만, 급속한 증가율을 감안할 때 올해 안에 20%를 넘을 전망(展望)이다. 미국의 경우 17년 말 현재 27%의 사이버 증권거래가 이루어지고 있으며, 앞으로 인터넷(Internet) 보급의 확대로 인해 그 비중은 더욱 확대될 전망이다.

        사이버 거래 증가 현황
        사이버 증권거래가 이처럼 크게 증가하고 있는 원인은 1년에 계좌당 평균 25건의 거래가 이루어지는 등 일일거래자(Day Trader)가 급격히 증가했기 때문인 것으로 알려졌다.
        25%~30%에 달하는 사이버 고객(顧客)이 일일거래의 75%~80%에 해당하는 거래를 행하는 것으로 추정되는 일일 거래자가 총 거래의 증가뿐만 아니라 사이버 거래 증가에 커다란 역할을 하는 것을 알 수 있다.
        미국 사이버증권 산업분석가인 CSFB증권에 따르면, 2018년에는 주식 주문 2건당 1건이 사이버 거래(去來)를 통해 이루어질 것으로 예측된다고 한다.

        사이버 증권거래의 장단점
        사이버 증권거래의 장점으로는 저렴한 가격(Low Price), 편리성(Convenience), 시간과 장소로부터의 자유로움(Overcome the limits to place and time), 일반 투자자들에 대한 풍부한 정보 제공(provides retail investors with the rich information on securities) 등이 있다.
        이러한 이점으로 인해 투자 활성화, 증권 시장의 유동성 증가, 거래의 활성화 등을 통해 기업의 자금(資金) 조달이 용이하게 된다.
        사이버 증권거래의 단점으로는 투기의 조장, 시스템 장애 시의 문제 발생, 전문적 지식을 가진 브로커로부터의 격리 등을 들 수 있다. 또한, 인터넷이 주식 투자의 새로운 채널로 보편화되면서 인터넷을 통한 초단기 주식매매 성행을 들 수 있다.

        참고문헌
        Whoopi Leibovitz(2011). The Power of Pilgrimage, GilbutSchool. pp25-29.
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.
        Loyd Gray(2008). Globe Merriam of Frogs Collection, Academy Press. pp32-45.""",
        
    "입주를 1년 이내 앞둔": 
        """개요
        입주를 1년 이내 앞둔 강남 지역 아파트 분양권에 투자(Investment) 겸용 수요(Demand)가 몰리고 있다. 강남 재건축(Reconstruction) 아파트 호가가 지속적으로 오르면서 새 아파트(Apartment)도 입주 시세(Current Price)가 더 오를 것으로 예상되기 때문이다.
        가격 상승폭이 취득, 등록세를 포함한 세금(Tax)을 웃돌면 팔고 가격이 주춤하면 임대나 실입주까지 감안(勘案)하는 것이다. 9월에 입주하는 서초구 방배동의 상공아파트의 경우 최근 한 달 사이 시세가 평형별로 2,000만 원에서 3,000만 원 가량 올랐다. 프리미엄(Premium)만 1억 3,000만 원에 달하는 아파트도 흔하다.

        일부 지역 특수
        지난달 31일 강남권 부동산 중개업계에 따르면 그동안 주춤하던 입주 임박 아파트에 대한 분양권 매수세가 6월 중순 이후 살아나고 있다.
        강남구의 입주 예정 1년 미만 분양권 가격(價格) 상승률은 지난 5월 0.2%로 바닥을 친 후 6월 0.87%, 7월 1.69%로 빠른 상승세(Upward Tendency)를 보이고 있다.
        서초구도 거래 가격 오름 폭이 크며 수도권 중 유일하게 분당구의 상승(Rising)이 두드러진다.

        매수세 이어질 듯
        강남, 서초 일대의 분양권 수요자들은 실입주가 목적(目的)이라고 시세 상승 가능성(Possibility)에 큰 관심을 보이고 있다는 것이 주변 공인중개소 관계자들(Interested Persons)의 말이다.
        특히, 그동안 여러 가지 이유(Reason)로 웃돈이 적게 붙었던 아파트는 분양권 투자자(Investor)의 주요 대상(Target)이 되고 있다. 곽영순 명성공인 사장은 “이런 분위기(Business Conditions)라면 단지 내 조경 공사(Landscape Architecture)가 시작 될 무렵에는 매수세가 더욱 살아날 것”으로 예상(豫想)했다.
        곳곳에 재건축 공사가 한창인 강남구도 사정은 비슷하다. 집주인들(Landlords)은 시세가 더 오를 것을 노려 매물(Offerings)을 내놓고 있지 않아 당분간 상승세는 지속될 것으로 보인다.

        참고문헌
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.
        Loyd Gray(2008). Globe Merriam of Frogs Collection, Academy Press. pp32-45.
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.""",
    
    "전국의 2인 이상 가구 수는": 
        """전국의 2인 이상 가구 수는 1,221만 가구이며, 차량등록대수는 1,206만 대이다. 이로써 우리는 사실상 1가구 1차량 시대에 접어들었다. 따라서 운전질서(Driving Order) 확립은 운전자라면 누구나 지켜야 할 생활(生活)의 기본이 되었다. 하지만 우리나라의 운전 질서 수준은 외국인들의 지적대로 엉망이 아닐 수 없다. 교통질서 확립을 위해서는 합리적인 도로 시스템도 질서유지의 요인이 되는 것을 알 수 있다. 독일의 경우, 정지선(Stop Line) 준수율이 90%가 넘는 비결은 신호등(Signal Lamp)의 위치 때문이다. 신호등이 정지선 바로 위에 낮게 설치되어 있어 정지선을 조금이라도 넘어가면 신호가 전혀 보이지 않게 되어 있다.

        각 국의 교통질서와의 비교
        교통안전공단(Korea Transportation Safety Authority)과 대한교통학회(Korean Society of Transportation)가 한국의 교통문화지수(Traffic-culture Index)를 일본의 오사카, 독일의 만하임(Mannheim)과 비교(比較)하여 발표(發表)하였다.
        횡단보도(Pedestrian Crossing) 정지선을 지키는 비율은 서울이 45.9%, 부산이 51.9%로 오사카의 67.9%나 독일의 92.6%에 비해 낮은 수치를 나타냈다.
        또한 안전띠(Safety Belt) 착용도 서울 38.9%, 부산 49.4%로 일본 오사카의 72.4%보다 훨씬 낮은 것으로 나타났다.
        손해보험협회(Nonlifes Insurance Society)가 시내운행 차량을 관찰한 결과, 교차로 통행 위반은 한국이 2.5명으로 일본의 0.2명보다 13배나 많은 수치를 나타냈다. 또한 끼어들기 위반차량도 1.8명으로 일본의 0.6명보다 3배나 많았다.

        변화를 위한 노력
        녹색교통운동은 “자신의 안전뿐만 아니라 타인의 생명(生命)과 행복(幸福)까지 앗아갈 수 있는 것이 교통질서 위반이다”라고 말했다.
        교통질서는 다른 사람에 대한 배려(Consideration)에서 나오는 것이므로 타인도 내 가족과 같이 여기는 마음으로 운전하는 습관이 중요하다고 강조했다.

        참고문헌
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.""",
                
    "전통적인 전자상거래 형태인": 
        """개요
        전통적인 전자상거래 형태인 전자적자료교환(Electronic Data Interchange, EDI)은 2015년 무역 부문에 EDI가 도입된 이래 매년 높은 증가율을 보이고 있다. 한국정보통신진흥협회에 따르면 2016년 EDI의 이용기관은 13,592개에서 2017년에는 19,000개로 증가하였으며, 2018년에는 26,000개에 달할 것으로 예상된다. EDI의 활용이 상대적으로 활발한 부문은 무역 및 통관과 유통 부문으로 무역 및 통관 부문은 약 10,400여 개의 업체가 EDI 기술을 사용하고 있으며, 유통 부문은 약 7,000개의 업체가 공급망 관리 차원에서 대형 유통업체를 중심으로 물품 공급업체와의 거래 업무에 사용하고 있다. 중소기업의 경우 경제적, 기술적인 부담으로 인해 EDI의 도입이 미진하다.

        EDI 향후 전망
        최근에 2018년부터 인터넷을 이용한 Web-EDI 서비스가 일부 VAN(Value-Added Network) 사업자를 통해 제공되면서 중소기업들의 EDI 도입이 점차 확산될 것으로 예상된다.
        Web-EDI는 인터넷에 접속할 수 있는 PC만 보유하면 EDI를 활용할 수 있기 때문에 EDI 확산의 기술적, 경제적 장벽을 크게 낮출 수 있다.
        실제 많은 중소기업들이 점차 Web-EDI를 활용하고 있는 것으로 파악된다.
        SG-Mart와 상공백화점 공급업체의 경우 많은 수의 중소업체가 2017년 중 Web-EDI를 도입하여 업무를 전자적으로 처리하고 있다.

        EDI 발전을 위한 제안
        인터넷(Internet)의 새로운 자료 표현 표준인 XML(eXtensible Markup Language)의 등장(登場)으로 XML/EDI라는 기업간 전자상거래의 새로운 구현기술이 개발되고 있다.
        XML은 HTML(Hyper Text Markup Language)과 달리 구조화된 표현 방식으로 거래에 따른 의미 있는 자료의 교환, 저장, 검색, 처리가 가능하여 앞으로 전자상거래(Electronic Commerce, EC)의 유력한 기술로 대두될 것이다.
        국내 기업들은 XML/EDI 기술(技術)을 이용한 새로운 기업간 전자상거래 시대를 대비해야 할 것이다.

        참고문헌
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.
        Wiliam. K. Narayan(2010). The Autobiography Urinalysis of the way to Samurai, Easy Press. pp56-89.""",
        
    "지난 5일 부시 미 대통령이": 
        """개요
        지난 5일 부시 미 대통령이 국내산업 보호(保護)를 위하여 미국의 국제무역위원회(ITC : International Trade Commission)에 외국산 철강제품에 대한 통상법 201조 즉, 긴급수입 제한조치(Safe Guard) 발동을 위한 실태조사를 요청했으며, 행정부는 철강과잉생산, 정부보조금(State Subsidy) 재원 등의 문제를 논의하기 위해 교역(交易) 대상국과 다자협상(Multilateral Negotiation)을 개시하겠다고 밝혔다.
        ITC는 통상법 201조에 따라 조사기간 중 피해 여부만을 조사하며 수출국들의 덤핑 여부나 덤핑률(Dumping Rate) 등에 대해서는 조사하지 않지만 이미 미국 철강업체들의 적자경영이 심화되고 있어 피해 판정이 거의 확실시된다.

        철강업계 전망
        내년에 취해질 수입규제로 다양한 조치가 예상되고 있다.
        각 국별로 철강수입 쿼터(Quota)를 정하거나 반덤핑 관세(Anti-Dumping Duties)를 부과하는 것이 가장 보편적인 것으로 보인다. 이 중에서 쿼터제의 실시가 가장 가능성이 높을 것으로 점쳐지고 있는데, 이미 미국 의회에서는 철강산업 부활법안(Steel Revitalization Act)이 제출(提出)되어 있기 때문이다.
        미국 철강수입량의 7.1%를 차지하며 4위를 차지하고 있는 우리나라도 미국으로부터 철강제품에 대한 수입제한 조치를 받고 있다. 지역별 수출비중은 미국, 유럽, 기타 순으로 나타난다.

        국내 철강업계에 큰 타격 예상
        미국 철강시장은 중국, 일본에 이어 전체 철강수출의 17.4%를 차지하는 3위의 시장을 형성하고 있다.
        IMF(International Monetary Fund) 이전 연간 약 150만 톤 수준이던 대미 수출물량은 2015년 340만 톤을 정점으로 점차 감소하고 있는 추세로 지난해는 230만 톤의 수출을 기록했다.
        미국이 통상법 201조를 발동할 경우엔 대미 철강수출 물량이 2014년 이전인 130만 톤 수준(水準)으로 떨어져 약 100만 톤이 줄어들 것으로 예상된다.

        참고문헌
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.
        Salame, R.(2006). Why Do Mergers Fail?, Key Strategy. pp28-32.
        A. S. Madison(2011). Learning to Dear Straw, Kindle Press. pp28-32.""",
        
    "지난달 서울지법 107호 경매 법정(Court)에서": 
        """개요
        지난달 서울지법 107호 경매 법정(Court)에서 역삼동 52.9(m2)인 아파트가 1억6,879만원을 써낸 A씨에게 돌아갔다. 이 아파트의 감정가는 1억3,000만원으로 감정가보다 30%나 비싸게 샀다. 경매 전문가(Specialist)들은 아파트의 경우 낙찰가율이 85%만 넘어도 수익성(Profit)이 거의 없다고 평가(Appraisement)하고 있다. 그런데 요즘은 역삼동의 경우처럼 낙찰가(ConTract Price)가 아예 감정가(an Appraised Value)를 뛰어넘는 경우가 훨씬 많다. 82.6(m2) 내외의 아파트들이 6월 11일 명일동에서 112%, 6월 4일 방화동에서 107%, 6월 7일 신정동에서 101%의 낙찰가율을 연이어 기록했다.

        달아오른 부동산 Auction
        초저금리와 불안한 증시(Stock Market) 등락에 갈 곳 모르던 투자자금(Capital)이 부동산에 몰렸고 경매로 좋은 물건을 잡을 수 있다는 입소문 속에 인기품목으로 대두했다는 논리(論理)이다.
        아파트 경매에서는 이미 고가낙찰을 예외적 사례로 볼 수 없는 상황이다.
        수도권의 아파트 낙찰가율은 5월(86.6%)과 6월(86.9%)에 업계가 꼽는 수익분기점(85%)을 넘어섰다. 평균치로 따져도 이익을 남기기는 어려운 지경에 이른 셈이다.
        아파트에서 넘쳐난 장기 여유자금은 근린, 단독, 연립주택과 토지에까지 흘러들고 있다.

        향후 전망
        부동산컨설팅(Real Estate Consulting) 업체(業體)의 이진우 자산관리팀장은 “현재의 낙찰가 수준(水準)이라면 차라리 급매로 사는 것이 유리한 경우가 많다”고 지적한다.
        Auction Consulting의 대표업체인 (주) 포드림(www.fordream.co.kr)의 오상윤 Analyst도 경매가 돈이 된다고들 하자 개미군단까지 몰려들어 “묻지마 투자”가 벌어지고 있다며 위험성을 경고한다.
        예금금리(Deposit Rate)가 낮아지고 금융기관들의 대출금리(Interest on a loan)가 낮아 돈을 꾸어서라도 투자(Investment)하려는 소규모 투자자인 개미군단들의 피해가 예상된다.

        참고문헌
        Wiliam. K. Narayan(2010). The Autobiography Urinalysis of the way to Samurai, Easy Press. pp56-89.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Whoopi Leibovitz(2011). The Power of Pilgrimage, GilbutSchool. pp25-29.""",
        
    "최근 국내 정보통신 산업은": 
        """개요
        최근 국내 정보통신 산업은 뚜렷한 하향세를 보이고 있다. 2017년 하반기 이후 컴퓨터, 통신, 반도체 등 정보통신 산업은 국내외 경기불안과 전년도 호황에 대한 기술적인 하락으로 성장률이 눈에 띠게 둔화되고 있다. 컴퓨터 산업은 IMF체제가 들어선 이후 수출과 내수 모두 초고속 성장을 거듭하여 80년대 후반의 옛 영광을 되찾는 듯했다. 그러나 수출(輸出)의 경우 증가율 둔화를 보이다가 11월에는 급기야 전년 대비 11.4%나 감소하는 등 급격히 위축되고 있다. 인터넷 붐과 함께 형성되었던 국내 내수기반도 국내 경기침체와 함께 성장세가 둔화되고 있는 실정이다. 정부(政府)에서 추진하던 인터넷 PC의 성장이 한계를 보이고 있고 교육용 PC의 성장세도 정부예산의 조기집행으로 하반기이후 탄력성을 잃고 있다.

        통신기기 내수 추이 분석
        국내 통신기기 내수(2017년 기준 통신기기 생산의 75%)는 무선 단말기의 빠른 보급으로 IMF체제 기간 중에도 성장을 지속해왔다.
        그러나 무선 통신 단말기의 보급률이 한계에 도달한데다 2017년 6월 이후 보조금 폐지로 수요(需要)가 급속히 줄어 2017년 9월 가입자 수가 전년 말 수준에 머무르고 있다.
        금년 들어 9월까지 무선통신기기의 내수는 전년 동기 대비 0.6%가 감소하였고 시간이 갈수록 감소 폭이 확대되고 있다(표 참조).

        통신기기 내수 향후 전망
        7월 중에 8.88달러에 이르던 64M DRAM(Dynamic Random Access Memory) 가격(價格)이 12월에는 3.09달러로 추락하였다.
        경제성장의 견인차 역할을 하던 반도체의 경우엔 올해 하반기 들어 가격이 급격하게 하락하는 양상을 보이고 있다.
        수출의 경우에는 GSM 단말기 수출과 모토롤라(Motorola Inc.) 등에 대한 주문자상표부착(OEM : Original Equipment Manufacturing) 방식 그리고 셋톱박스(Settop Box), 중국의 CDMA(Code Division Multiple Access) 채택 등 수요확대 요인(要因)이 없는 것은 아니지만 하락기에 들어간 국내 정보통신 산업의 고성장은 당분간 매우 어려울 것으로 보인다.

        참고문헌
        Loyd Gray(2008). Globe Merriam of Frogs Collection, Academy Press. pp32-45.
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Guillen, M.(2008). Building a Global Bank, Princeton University Press. pp34-45.""",
        
    "컴퓨터를 이용한 인터넷 경매가": 
        """개요
        컴퓨터를 이용한 인터넷 경매가 인터넷 비즈니스(Internet Business)의 꽃으로 떠오르고 있다. 인터넷 경매(Internet Auction)에서는 수요자와 공급자가 인터넷 공간에서 직접 만나 서로 흥정해 물건(物件)을 사고판다. 즉 유통업체들이 일방적으로 가격을 정해 파는 쇼핑몰(Shopping Mall)보다 훨씬 합리적이고 유망한 거래방식이다.
        기존 경매방식과의 가장 큰 차이는 모든 정보(情報)가 인터넷을 통해 실시간(Real Time)으로 서비스가 이루어지므로 공간의 제약에서 벗어날 수 있으며, 이런 장점 때문에 인터넷을 통해 개인과 개인이 직접 만나는 소비자간(Consumer to Consumer) 전자상거래(Electronic Commerce)는 21세기에 가장 유망한 인터넷 비즈니스로 주목을 받고 있다.

        인터넷 경매의 전망
        인터넷 시장(Internet Marketing) 분석기관인 키넌비전(Keenan Vision)은 최근 2017년 38억 달러였던 미국의 온라인 경매실적이 2022년에는 1,290억 달러로 폭증할 것이라고 밝혔다.
        온라인 경매(On-Line Auction) 참여자도 2012년 300만 명에서 2022년에는 1,400만 명으로 늘어나며 참여업체는 5,000개로 증가할 것으로 예상하였다.
        인터넷 경매는 소비자와 기업간에 정보를 중개(仲介)하는 비즈니스(Business)로부터 다양한 효과(Effect)가 나타나고 있다.
        C2C 전자상거래는 인터넷 경매 외에 각종 상품과 서비스를 실수요자끼리 사고파는 생활정보지 방식 서비스가 있다. 개인 홈페이지(Homepage) 보급이 늘면서 별도 사이트(Site)를 통하지 않고 홈페이지에서 직접 거래를 하는 일도 급증할 전망이다.

        인터넷 경매의 장점
        경매와 역경매에서는 소비자 자신이 붙인 가격(價格)에 상품을 구입할 수 있게 된다.
        상품명을 지정하게 되면 Internet 상의 복수 숍에서 판매(販賣)되고 있는 같은 상품을 검색하여 가격과 판매조건을 즉석에서 비교하여 표시하는 사이트가 있지만, 이것 역시 소비자를 유리하게 하는 정보 중개(Information Agency)인 것이다.
        소비자의 입장에 서서 사업을 행하는 기업이 경쟁우위를 확보하게 될 것이다.

        참고문헌
        R. K. Dragon(2006). A Civil Organic Modern Chemistry, Gilbut. pp34-56.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.
        Whoopi Leibovitz(2011). The Power of Pilgrimage, GilbutSchool. pp25-29.""",
        
    "통계청(National Statistical Office)은": 
        """개요
        통계청(National Statistical Office)은 ‘통계로 본 한국 여성의 삶’이라는 자료(資料)를 펴냈다. 이 통계 자료(Data)에는 ‘여성의 대학 진학률(the Rate of Entrance into a School of Higher Grade)이 계속해서 늘어 남성과 차이를 줄였으며 여성의 47.6%는 술을 마시고 4.6%는 담배를 피운다’는 등 재미있는 자료들이 많이 담겨 있다. 그러나 이 통계는 단순한 재미만을 제공(提供)하는 것이 아니라, 우리 사회의 성차별 문제가 여전히 심각함을 드러내는 것이 많아 주목된다. 여성의 경제활동(Economic Activity) 참가율이 계속해서 증가한다는 측면에서 고무적인 일이라고 할 수 있다. 그러나 그 실상을 들여다보면 그렇지 않다. 초등교사의 여성 비율이 압도적으로 높은 반면, 보직교사의 비율은 남성이 압도적으로 높게 나타난다. 이것은 뿌리깊은 성차별적 관행을 보여주는 전형적인 예라 하겠다.

        성차별 사례
        명예퇴직을 한 교사와 평교사의 경우는 여성의 비율이 압도적으로 높다.
        초등학교(Elementary School) 교사의 3명 가운데 2명은 여교사라는 통계(統計)가 나왔다.
        서울지역은 여교사 비율이 77.9%로 가장 높으며 전남 지역은 45.3%로 가장 낮다.

        관련법은 선진국 수준
        모성 보호(保護)와 육아(Child Care)에 대한 사회적 지원을 보장하는 법은 헌법(the Constitutional Law)의 모성보호법, 남녀고용평등법(육아휴직, 직장 보유시설 의무), 영유아보육법(보육시설), 국가공무원법(육아휴직) 등 선진국 수준(水準)으로 다양하게 규정되어 있다.
        국가공무원 규정에도 여성 공무원의 출산휴가(Maternity Leave), 보건휴가, 임신중 검진휴가, 육아시간 등이 보장되어 있다.
        그러나 한국여성 개발원 김엘림 수석연구원은 “법규 준수 실태에 대한 정확한 조사 통계도 없는 실정”이라며 “지방 공무원(a Local Civil Servants)의 경우 대체 인력이 부족해 현행 60일도 채우지 못하는 경우가 적지 않다”고 지적하고 있다.

        ※ 참고문헌
        Jerry Vanzant(2012). The Emergence of Puddiing Away, ABC Press. pp13-25.
        Guillen, M.(2008). Building a Global Bank, Princeton University Press. pp34-45.
        Nunes, T. et al.(2005). The Privatization of Banespa, Business Case Study. pp27-45.""",

}

# --- CÁC HÀM XỬ LÝ LOGIC ---
def normalize_text(text, mode):
    if not text: return ""
    if mode == "Nới lỏng (Bỏ qua lỗi dư Khoảng trắng / Enter)":
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    else:
        return text.strip()

def generate_visual_diff(original, student):
    matcher = difflib.SequenceMatcher(None, original, student)
    orig_html = []
    stud_html = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        o_chunk = original[i1:i2].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        s_chunk = student[j1:j2].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        
        if tag == 'equal':
            orig_html.append(f"<span>{o_chunk}</span>")
            stud_html.append(f"<span>{s_chunk}</span>")
        elif tag == 'delete':
            orig_html.append(f"<span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>{o_chunk}</span>")
        elif tag == 'insert':
            stud_html.append(f"<span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>{s_chunk}</span>")
        elif tag == 'replace':
            orig_html.append(f"<span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>{o_chunk}</span>")
            stud_html.append(f"<span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>{s_chunk}</span>")
            
    box_template = """
    <div style="border: 1px solid #ccc; border-radius: 5px; padding: 15px; height: 350px; overflow-y: auto; background-color: white; color: black; font-size: 16px; font-family: 'Malgun Gothic', sans-serif; line-height: 1.6;">
        {content}
    </div>
    """
    return box_template.format(content="".join(orig_html)), box_template.format(content="".join(stud_html))

# --- GIAO DIỆN NGƯỜI DÙNG ---
st.title("🖥️ Hệ thống chấm điểm gõ văn bản - Phiên bản Bài mẫu tích hợp")
st.markdown("Hệ thống tự động lưu trữ 25 bài mẫu. Thầy chỉ cần chọn bài và dán bài làm của sinh viên.")

# Khung chọn luật chấm điểm và chọn bài mẫu
st.subheader("⚙️ Cấu hình chấm thi")
config_col1, config_col2 = st.columns(2)

with config_col1:
    scoring_mode = st.radio(
        "Luật xử lý Khoảng trắng (Space) và Enter:",
        ("Nới lỏng (Bỏ qua lỗi dư Khoảng trắng / Enter)", "Khắt khe (Tính chính xác tuyệt đối từng Dấu cách / Enter)")
    )

with config_col2:
    # Tạo danh sách lựa chọn bài mẫu + Thêm 1 tùy chọn tự nhập nếu muốn
    options = list(DANH_SACH_BAI_MAU.keys()) + ["--- Tự nhập văn bản gốc mới ---"]
    selected_option = st.selectbox("Chọn văn bản gốc từ danh sách bài mẫu:", options)

st.divider()

# Xác định nội dung văn bản gốc dựa trên lựa chọn
if selected_option == "--- Tự nhập văn bản gốc mới ---":
    text_origin_input = st.text_area("✍️ Dán nội dung văn bản gốc MỚI vào đây:", height=150)
else:
    # Lấy nội dung từ danh sách mẫu có sẵn
    text_origin_input = DANH_SACH_BAI_MAU[selected_option]
    # Hiển thị cho thầy xem trước (nhưng khóa lại không cho sửa để tránh bấm nhầm)
    st.text_area(f"📖 Nội dung gốc của [{selected_option}]:", text_origin_input, height=100, disabled=True)

# Khung nhập bài làm sinh viên
st.subheader("🎓 Bài làm của Sinh viên")
raw_student = st.text_area("Dán bài làm của sinh viên vào đây để đối chiếu:", height=200, key="stud_text")

# Nút chấm điểm
if st.button("🚀 BẮT ĐẦU CHẤM ĐIỂM", use_container_width=True, type="primary"):
    if not text_origin_input or not raw_student:
        st.warning("Vui lòng đảm bảo đã có nội dung Văn bản gốc và Bài làm của sinh viên.")
    else:
        with st.spinner("Hệ thống đang đối chiếu dữ liệu..."):
            norm_original = normalize_text(text_origin_input, scoring_mode)
            norm_student = normalize_text(raw_student, scoring_mode)
            
            matcher = difflib.SequenceMatcher(None, norm_original, norm_student)
            score = matcher.ratio() * 100
            
            st.success("✅ Đã chấm điểm xong!")
            st.metric("Điểm số tương đồng", f"{score:.2f}%", f"Chế độ: {scoring_mode.split(' ')[0]}")
            
            st.markdown("### 🔍 Phân tích chi tiết lỗi sai")
            st.markdown("""
            * <span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>Gạch đỏ:</span> Ký tự gốc sinh viên gõ thiếu hoặc gõ sai.
            * <span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>Gạch xanh dương:</span> Ký tự sinh viên gõ thừa hoặc gõ sai thay thế vào.
            """, unsafe_allow_html=True)
            
            diff_orig_html, diff_stud_html = generate_visual_diff(norm_original, norm_student)
            
            diff_col1, diff_col2 = st.columns(2)
            with diff_col1:
                st.markdown("**Văn bản Gốc:**")
                st.markdown(diff_orig_html, unsafe_allow_html=True)
            with diff_col2:
                st.markdown("**Bài gõ của Sinh viên:**")
                st.markdown(diff_stud_html, unsafe_allow_html=True)
