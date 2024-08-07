from collections import defaultdict
from kobert_tokenizer import KoBERTTokenizer
import os
import pickle
import logging

# from glob import glob


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/log.log",
    level=logging.DEBUG,
    format="[%(asctime)s | %(funcName)s @ %(pathname)s] %(message)s",
)
logger = logging.getLogger()


class DataChunk:
    """인풋 text를 tokenizing한 뒤에 주어진 길이로 chunking 해서 반환합니다. 이때 하나의 chunk(context, index 단위)는 하나의 article에만 속해있어야 합니다."""

    def __init__(self, chunk_size=100):
        self.chunk_size = chunk_size
        self.tokenizer = KoBERTTokenizer.from_pretrained("skt/kobert-base-v1")
#         strings = '''
#         분만의 과정
#  포인트: 분만은 여성에게서 정상적인 생리과정으로 대부분은 합병증 없이 
# 일어나지만 합병증 발생시는 빠르고 예측 불가능하게 진행
#  휴지기: 자궁 근육의 고유기능인 수축성을 없고 평활근이 자연적인 
# 자극에 반응하지 않는 시기
#  준비기: 진통을 위한 준비 시기
#  활성 진통기: 자궁 수축이 일어나면서 자궁경관 개대와 태아의 분만이
# 이루어지는 시기
#  1기: 자궁 경부가 완전 개대(10 cm)될 때까지의 기간
#  2기: 자궁 경관이 완전 개대된 이후부터 태아 분만까지의 시기
#  3기: 태아분만 직후부터 태반과 태아막의 분만까지의 시기
#  산욕기: 분만 후 회복과 유아의 생존을 위한 역할과 분만 후 수태력의 회복기 첫번째
#         분만의 과정
#  포인트: 분만은 여성에게서 정상적인 생리과정으로 대부분은 합병증 없이 
# 일어나지만 합병증 발생시는 빠르고 예측 불가능하게 진행
#  휴지기: 자궁 근육의 고유기능인 수축성을 없고 평활근이 자연적인 
# 자극에 반응하지 않는 시기
#  준비기: 진통을 위한 준비 시기
#  활성 진통기: 자궁 수축이 일어나면서 자궁경관 개대와 태아의 분만이
# 이루어지는 시기
#  1기: 자궁 경부가 완전 개대(10 cm)될 때까지의 기간
#  2기: 자궁 경관이 완전 개대된 이후부터 태아 분만까지의 시기
#  3기: 태아분만 직후부터 태반과 태아막의 분만까지의 시기
#  산욕기: 분만 후 회복과 유아의 생존을 위한 역할과 분만 후 수태력의 회복기 두번째
#         분만의 과정
#  포인트: 분만은 여성에게서 정상적인 생리과정으로 대부분은 합병증 없이 
# 일어나지만 합병증 발생시는 빠르고 예측 불가능하게 진행
#  휴지기: 자궁 근육의 고유기능인 수축성을 없고 평활근이 자연적인 
# 자극에 반응하지 않는 시기
#  준비기: 진통을 위한 준비 시기
#  활성 진통기: 자궁 수축이 일어나면서 자궁경관 개대와 태아의 분만이 두번째 반
#         '''
#         print(self.tokenizer.decode(self.tokenizer.encode(strings, max_length=512)))
#         assert False
    def chunk(self, input_file):
        """input file format은 attardi/wikiextractor에 나온 형태를 따릅니다."""
        with open(input_file, "rt", encoding="utf8") as f:
            input_txt = f.read().strip()
        input_txt = input_txt.split(
            "</doc>"
        )  # </doc> 태그로 split하여 각 article의 제목과 본문을 parsing합니다.
        chunk_list = []
        orig_text = []
        #dawon code start

        for art in input_txt:
            art = art.strip()
            if not art:
                logger.debug(f"article is empty, passing")
                continue
            
            #title = art.split("\n")[0].strip(">").split("title=")[1].strip('"')
            #text = "\n".join(art.split("\n")[2:]).strip()

#             encoded_title = self.tokenizer.encode(title)
#             encoded_txt = self.tokenizer.encode(text)
#             if len(encoded_txt) < 5:  # 본문 길이가 subword 5개 미만인 경우 패스
#                 logger.debug(f"title {title} has <5 subwords in its article, passing")
#                 continue
            chunk = self.tokenizer.encode(art)
            orig_text.append(self.tokenizer.decode(chunk))
            chunk_list.append(chunk)

            # article마다 chunk_size 길이의 chunk를 만들어 list에 append. 각 chunk에는 title을 prepend합니다.
            # ref : DPR paper
#             for start_idx in range(0, len(encoded_txt), self.chunk_size):
#                 end_idx = min(len(encoded_txt), start_idx + self.chunk_size)
#                 chunk = encoded_title + encoded_txt[start_idx:end_idx]
#                 orig_text.append(self.tokenizer.decode(chunk))
#                 chunk_list.append(chunk)
        return orig_text, chunk_list


def save_orig_passage(
    input_path="text", passage_path="processed_passages", chunk_size=100
):
    """store original passages with unique id"""
    os.makedirs(passage_path, exist_ok=True)
    app = DataChunk(chunk_size=chunk_size)
    idx = 0
    for path in tqdm(glob(f"{input_path}/*/wiki_*")):
        ret, _ = app.chunk(path)
        to_save = {idx + i: ret[i] for i in range(len(ret))}

        with open(f"{passage_path}/{idx}-{idx+len(ret)-1}.p", "wb") as f:
            pickle.dump(to_save, f)
        idx += len(ret)
        # break


def save_title_index_map(
    index_path="title_passage_map.p", source_passage_path="processed_passages"
):
    """korquad와 klue 데이터 전처리를 위해 title과 passage id를 맵핑합니다.
    title_index_map : dict[str, list] 형태로, 특정 title에 해당하는 passage id를 저장합니다.
    """
    logging.getLogger()

    files = glob(f"{source_passage_path}/*")
    title_id_map = defaultdict(list)
    for f in tqdm(files):
        with open(f, "rb") as _f:
            id_passage_map = pickle.load(_f)
        for id, passage in id_passage_map.items():
            title = passage.split("[SEP]")[0].split("[CLS]")[1].strip()
            title_id_map[title].append(id)
            #print(title[:10],"thatistrue\n",id)
        logger.info(f"processed {len(id_passage_map)} passages from {f}...")
    with open(index_path, "wb") as f:
        pickle.dump(title_id_map, f)
    logger.info(f"Finished saving title_index_mapping at {index_path}!")


if __name__ == "__main__":
    # 디버깅용 main
    # import argparse
    from tqdm import tqdm
    from glob import glob

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--chunk_size', type=int, default=100)
    # args = parser.parse_args()
    # app = DataChunk(chunk_size = args.chunk_size)
    # item = []
    # num = 0
    # for i,path in enumerate(tqdm(glob('result/*/wiki_*'))):
    #     ret = app.chunk(path)
    #     # item.append(max([len(e) for e in ret]))
    #     num += len(ret)
    #     # if i > 9 : break
    # print(f'total number of passages : {num}')
    # print(f"max length of passage : {max(item)}")
    save_orig_passage()
    save_title_index_map()
