# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional
from ast import literal_eval
import fire
import sys
import json
import jsonlines
from llama import Llama
from tqdm import tqdm

template1 = ""
template2 = ""

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 2048,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    final=[]
    count=-1
    cur_dial=[]
    current=""
    persona_pool = []
    print("start------")
    with jsonlines.open("./bigdata/test2.jsonl",'r') as f:
        for line in f:
            for s1p in line['session1_persona']:
                persona_pool.append(s1p)
            for s2p in line['session2_persona']:
                persona_pool.append(s2p)
            for idx,cu in enumerate(line['current']):
                current += f"{idx+1} : "+cu+"\n"
                
            user1={
                "role": "user", 
                "content": ""
            }
            assist={
                "role": "assistant",
                "content":""
            }
            user2={"role": "user", "content": ""}
            assist2={
                "role": "assistant",
                "content":""
            }
            userlist = []
            for persona in persona_pool:
                userlist.append(\        {"role":"user","content":template1+persona+template2+current})
            samplelist = []
            for user3 in userlist:
                samplelist.append([user1,assist,user2,assist2,user3])
        
            final.append(samplelist)
    print(len(final))
 
    persona_list=[]
    for i in tqdm(range(len(final))):
        results = generator.chat_completion(
            final[i],  # type: ignore
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )
        for dialog, result in zip(final[i], results):
            #for msg in dialog:
            #    print(f"{msg['role'].capitalize()}: {msg['content']}\n")
            #print(
            #    f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
            #)
            persona_list.append(result['generation']['content'])
    #print(len(persona_list))
            #print("\n==================================\n")
    with open("./bigdata/session4_selected_persona_list.txt",'w') as f:
        #index=0
        for t in range(0,len(persona_list),3):
            f.writelines("--session 1 persona list--: \n")
            f.writelines(persona_list[t]+'\n')
            f.writelines("--session 2 persona list--: \n")
            f.writelines(persona_list[t+1]+'\n')
            f.writelines("--session 3 persona list--: \n")
            f.writelines(persona_list[t+2]+'\n')
            f.writelines("--current dialogue--: \n")
            f.writelines(str(current[t//3])+"\n")
            #index+=1


if __name__ == "__main__":
    fire.Fire(main)