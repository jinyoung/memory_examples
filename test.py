from mem0 import Memory
from dotenv import load_dotenv


load_dotenv()

config = {
    "vector_store": {
        "provider": "supabase",
        "config": {
            "connection_string": "postgresql://postgres:postgres@localhost:54322/postgres",
            "collection_name": "memories",
            "index_method": "hnsw",  # Optional: defaults to "auto"
            "index_measure": "cosine_distance"  # Optional: defaults to "cosine_distance"
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": "123456789"
        }
    }
}

m = Memory.from_config(config_dict=config)


        
# m.add("기본 법인세율: 20%", user_id="alice")
# m.add("최대 감면율: 20% (중복 적용 가능하나 상한선 존재)", user_id="alice")
# m.add("업종별 제한: 제조업은 지방세 감면 제외, IT 서비스업은 여성 대표 + 지방 감면 동시 적용 가능", user_id="alice")
# m.add("신생 법인 감면: 설립 3년 이내 법인은 기본세율에서 10%를 감면", user_id="alice")
# m.add("여성 대표 감면: 대표이사가 여성인 경우 5% 추가 감면", user_id="alice")
# m.add("지역 감면: 비수도권 소재 기업은 지방세 3% 추가 감면", user_id="alice")
# m.add("소규모 신생 기업: 연매출 1억원 이하 & 설립 1년 미만은 전액 면제", user_id="alice")
# m.add("I like pizza", user_id="alice")


# m.add("제안서 작성 시 고려사항:\n\n1. 문서 형식 요구사항:\n- 공공기관: HWP 또는 정부 양식 필수\n- 민간기업: PPT 선호 (일부 PDF 문서형 요구)\n- 상장기업: IR 가치 제안 항목 필수 포함\n\n2. 평가 유형별 중점 사항:\n- 기술 중심: 아키텍처 다이어그램, 기능 명세 강조\n- 가격 중심: 비용 상세 내역, 유지보수 조건 강조\n- 성과 중심: 유사 사례, 성공사례 강조\n\n3. 특수 요구사항:\n- 보안 민감 기업: 데이터 보안 항목, 서버 위치 명시 필수\n- 검토 프로세스: 일반 기업 최소 1회, 공공기관 최소 2회 내부 검토 필수", user_id="alice")

# print(m.search("지방에 있는 매출에 설립일 1년 이내 여자 대표이사가 운영하는 회사이다. 이 회사의 법인세 감면율을?", user_id="alice"))
# print(m.search("유엔진은 서울에 있는 매출에 20억 이상의 남자 대표이사가 운영하는 회사이다. 이 회사의 법인세 감면율을?", user_id="alice"))
# print(m.search("공공기관에 제안서를 제출하려면 어떤 사항을 고려해야 하는가?", user_id="alice"))




# m.add("Basic corporate tax rate: 20%", user_id="alice")
# m.add("Maximum deduction rate: 20% (can be applied in combination, but there is a limit)", user_id="alice")
# m.add("Industry-specific restrictions: Manufacturing is excluded from local tax deductions, IT service companies can apply for female representative + local tax deductions at the same time", user_id="alice")
# m.add("Newly established corporate tax deduction: Corporations established within 3 years can deduct 10% from the basic tax rate", user_id="alice")
# m.add("Female representative tax deduction: An additional 5% deduction if the CEO is female", user_id="alice")
# m.add("Local tax deduction: Companies located in non-metropolitan areas can deduct an additional 3% from local taxes", user_id="alice")
# m.add("Small and medium-sized newly established companies: Companies with annual sales of less than 100 million won and established within 1 year are fully exempt", user_id="alice")
# m.add("I like pizza", user_id="alice")


# m.add("Considerations when writing a proposal:\n\n1. Document format requirements:\n- Public institutions: HWP or government forms are required\n- Private companies: Prefer PPT (some require PDF document format)\n- Listed companies: IR value proposal items must be included\n\n2. Key points for evaluation by type:\n- Technology-centric: Emphasize architecture diagrams, function specifications\n- Price-centric: Emphasize detailed cost details, maintenance conditions\n- Performance-centric: Emphasize similar cases, successful cases\n\n3. Special requirements:\n- Sensitive companies: Data security items, server location must be specified\n- Review process: At least 1 internal review for general companies, at least 2 internal reviews for public institutions", user_id="alice")

print(m.search("What is the corporate tax deduction rate for a company operated by a female representative director established within 1 year in a region with sales?", user_id="alice"))
print(m.search("What is the corporate tax deduction rate for a company operated by a male representative director with sales of over 20 billion in Seoul?", user_id="alice"))
print(m.search("What should be considered when submitting a proposal to a public institution?", user_id="alice"))
