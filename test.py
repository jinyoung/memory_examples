from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": "tm8kR4aa33FW52E"
        }
    }
}

m = Memory.from_config(config_dict=config)


        
m.add("기본 법인세율: 20%", user_id="alice")
m.add("최대 감면율: 20% (중복 적용 가능하나 상한선 존재)", user_id="alice")
m.add("업종별 제한: 제조업은 지방세 감면 제외, IT 서비스업은 여성 대표 + 지방 감면 동시 적용 가능", user_id="alice")
m.add("신생 법인 감면: 설립 3년 이내 법인은 기본세율에서 10%를 감면", user_id="alice")
m.add("여성 대표 감면: 대표이사가 여성인 경우 5% 추가 감면", user_id="alice")
m.add("지역 감면: 비수도권 소재 기업은 지방세 3% 추가 감면", user_id="alice")
m.add("소규모 신생 기업: 연매출 1억원 이하 & 설립 1년 미만은 전액 면제", user_id="alice")
m.add("I like pizza", user_id="alice")

print(m.search("유엔진은 서울에 있는 매출에 20억 이상의 남자 대표이사가 운영하는 회사이다. 이 회사의 법인세 감면율을?", user_id="alice"))


