# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '2,3,4'
from typing import Optional
from ast import literal_eval
import fire
import sys
import json
import jsonlines
from llama import Llama
from tqdm import tqdm

IN_FILE = "./bigdata/extracted_persona_session3.jsonl"
OUT_FILE = "./bigdata/session3_selected_persona.txt"


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
    
    write_string = ""
    max_lines = 0
    with open(OUT_FILE,'w') as f:
        pass
    print("start------")
    with jsonlines.open(IN_FILE,'r') as f:
        for i in f:
            max_lines += 1
    with jsonlines.open(IN_FILE,'r') as f:
        for numdialogue,line in enumerate(f):
            print(f"{numdialogue}/{max_lines}")
#             if numdialogue > 2:
#                 break
            persona_pool=""
            current_list=[]
            current=""
            current_buf=""
            with open(OUT_FILE,'a') as f:
                #f.writelines(f"Dialogue {numdialogue}:\n")
                write_string+=f"Dialogue {numdialogue}:\n"
            for idx,pers in enumerate(line['session1_persona']+line['session2_persona']):
                persona_pool+=f"P{idx+1}-"+pers+"\n"
            for idx,cu in enumerate(line['current']):
                current_list.append(f"C{idx+1}-"+cu+"\n")
                if len(current_list) > 4:
                    current_list = current_list[1:]
                
                current="".join(current_list)
                current_buf=f"C{idx+1}-"+cu+"\n"
                
                user1={
                    "role": "user", 
                    "content": 
                    "You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue.\n\nDialogue:\nC1-Speaker 1: I've booked myself a week long vacation from work next month!\n\nPersona Pool:\nP1-Speaker 1 needs advice on vacation.\nP2-Speaker 1 has been working non-stop with crazy hours.\nP3-Speaker 1 prefers the beach.\nP4-Speaker 1 loves brownies.\nP5-Speaker 2 has been all over the world (military background).\nP6-Speaker 2 has experience blowing things up.\nP7-Speaker 2 likes cute and cuddly kittens.\nP8-Speaker 2 prefers repetitive and exotic destinations (Bora Bora).\nP9-Speaker 2 loves chocolate (brownies).\nP10-Speaker 1 is a mechanical engineer\nP11-Speaker 1 can relate to working in the military and as an engineer\nP12-Speaker 1 is impressed by Speaker 2's work as an electrical engineer\nP13-Speaker 1 is aware of the importance of safety in the home\nP14-Speaker 1 has a cousin who had to spend a lot of money to bring their home up to code\nP15-Speaker 2 is an electrical engineer\nP16-Speaker 2 served in the military and is trained in electrical engineering\nP17-Speaker 2 works for a private company troubleshooting and installing equipment\nP18-Speaker 2 is good at their job and enjoys it\nP19-Speaker 2 is aware of the variety of households and their wiring configurations\nP20-Speaker 2 values safety in the home, especially for their children.\n\nTarget Utterance:\nC1-Speaker 1: I've booked myself a week long vacation from work next month!\nSelcted Persona:\n"
                }
                assist1={
                    "role": "assistant",
                    "content":"P1-Speaker 1 needs advice on vacation."
                }
                user2={"role": "user", "content": "You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue.\n\nDialogue:\nC1-Speaker 1: I've booked myself a week long vacation from work next month!\nC2-Speaker 2: How nice! Where are you going?\n\nPersona Pool:\nP1-Speaker 1 needs advice on vacation.\nP2-Speaker 1 has been working non-stop with crazy hours.\nP3-Speaker 1 prefers the beach.\nP4-Speaker 1 loves brownies.\nP5-Speaker 2 has been all over the world (military background).\nP6-Speaker 2 has experience blowing things up.\nP7-Speaker 2 likes cute and cuddly kittens.\nP8-Speaker 2 prefers repetitive and exotic destinations (Bora Bora).\nP9-Speaker 2 loves chocolate (brownies).\nP10-Speaker 1 is a mechanical engineer\nP11-Speaker 1 can relate to working in the military and as an engineer\nP12-Speaker 1 is impressed by Speaker 2's work as an electrical engineer\nP13-Speaker 1 is aware of the importance of safety in the home\nP14-Speaker 1 has a cousin who had to spend a lot of money to bring their home up to code\nP15-Speaker 2 is an electrical engineer\nP16-Speaker 2 served in the military and is trained in electrical engineering\nP17-Speaker 2 works for a private company troubleshooting and installing equipment\nP18-Speaker 2 is good at their job and enjoys it\nP19-Speaker 2 is aware of the variety of households and their wiring configurations\nP20-Speaker 2 values safety in the home, especially for their children.\n\nTarget Utterance:\nC2-Speaker 2: How nice! Where are you going?\nSelected Persona:\n"}
                assist2={"role": "assistant",
                    "content":"P1-Speaker 1 needs advice on vacation."}
                user3={"role": "user", "content": "You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue.\n\nDialogue:\nC1-Speaker 1: I've booked myself a week long vacation from work next month!\nC2-Speaker 2: How nice! Where are you going?\nC3-Speaker 1: Did not decided yet, I'd like to get an idea about traveling as you are big traveller.\nC4-Speaker 2: I like relaxing places, like the beaches. I love New Orleans, the entertainment is great there. That is where I'm going on my next vacation. What is your cousin going to do about the wiring in his house?\n\nPersona Pool:\nP1-Speaker 1 needs advice on vacation.\nP2-Speaker 1 has been working non-stop with crazy hours.\nP3-Speaker 1 prefers the beach.\nP4-Speaker 1 loves brownies.\nP5-Speaker 2 has been all over the world (military background).\nP6-Speaker 2 has experience blowing things up.\nP7-Speaker 2 likes cute and cuddly kittens.\nP8-Speaker 2 prefers repetitive and exotic destinations (Bora Bora).\nP9-Speaker 2 loves chocolate (brownies).\nP10-Speaker 1 is a mechanical engineer\nP11-Speaker 1 can relate to working in the military and as an engineer\nP12-Speaker 1 is impressed by Speaker 2's work as an electrical engineer\nP13-Speaker 1 is aware of the importance of safety in the home\nP14-Speaker 1 has a cousin who had to spend a lot of money to bring their home up to code\nP15-Speaker 2 is an electrical engineer\nP16-Speaker 2 served in the military and is trained in electrical engineering\nP17-Speaker 2 works for a private company troubleshooting and installing equipment\nP18-Speaker 2 is good at their job and enjoys it\nP19-Speaker 2 is aware of the variety of households and their wiring configurations\nP20-Speaker 2 values safety in the home, especially for their children.\n\nTarget Utterance:\nC4-Speaker 2: How nice! Where are you going?\nSelected Persona:\n"}
                assist3={"role": "assistant",
                    "content":"P14-Speaker 1 has a cousin who had to spend a lot of money to bring their home up to code"}
                user4={"role": "user", "content": "You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue.\n\nDialogue:\nC1-Speaker 1: I'm trying a new diet for my blood sugar.\nC2-Speaker 2: Is your blood sugar high?\n\nPersona Pool:\nP1-Speaker 1 is at home with three dogs.\nP2-Speaker 1 teaches drums and plays them well.\nP3-Speaker 1 works out to stay healthy.\nP4-Speaker 1 has a problem with blood sugar.\nP5-Speaker 2 is reading for an exam.\nP6-Speaker 2 wants to get a pit bull when they are done with school.\n\nTarget Utterance:\nC2-Speaker 2: It is good news. Is your blood sugar high?\nSelected Persona:\n"}
                assist4={"role": "assistant",
                    "content":"P4-Speaker 1 has a problem with blood sugar."}
                user5={"role": "user", "content": "You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue.\n\nDialogue:\nC3-Speaker 1: It's high. How's your mom managing hers?\nC4-Speaker 2: She's on medication and a diet. Have you started working out?\nC5-Speaker 1: I dislike working out. I hope my diet avoids the need for meds. Ever heard of keto?\nC6-Speaker 2: No, but I'll look into it for my mom. How are your dogs?\n\nPersona Pool:\nP1-Speaker 1 is at home with three dogs.\nP2-Speaker 1 teaches drums and plays them well.\nP3-Speaker 1 works out to stay healthy.\nP4-Speaker 1 has a problem with blood sugar.\nP5-Speaker 2 is reading for an exam.\nP6-Speaker 2 wants to get a pit bull when they are done with school.\n\nTarget Utterance:\nC6-Speaker 2: I never heard of it but I will read about it because it could be usefull for my mom. How are your dogs doing?\nSelected Persona:\n"}
                assist5={"role": "assistant",
                    "content":"P1-Speaker 1 is at home with three dogs."}
                user6={}
                user6["role"]="user"
                user6["content"]="You will be provided with a series of dialogues under Dialogue and a list of personas under Persona Pool. Your task is to read the dialogues and then identify which persona from the Persona Pool best matches or relates to the last dialogue in the Dialogue. Answer in the same form as in the previous example.\n\nDialogue:\n"+current+"\nPersona Pool:\n"+persona_pool+"\nTarget Utterance:\n"+current_buf+"\nSelected Persona:\n"
            
                #sample=[user1,assist1,user2,assist2,user3,assist3,user4,assist4,user5,assist5,user6]
                #sample=[user4,assist4,user5,assist5,user6]
                sample=[user5,assist5,user6]
                results = generator.chat_completion(
                [sample],  # type: ignore
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,
                )
                with open(OUT_FILE,'a') as f:
#                     f.writelines(f"Utterance {idx}: \n")
#                     f.writelines(cu+'\n')
#                     f.writelines(f"Selected Persona: \n")
               
#                     f.writelines(results[0]["generation"]["content"]+'\n')
                    write_string+=f"Utterance {idx}: \n"+cu+'\n'+f"Selected Persona: \n"+results[0]["generation"]["content"]+'\n'
    
            
    with open(OUT_FILE,'w') as f:
        f.writelines(write_string)
if __name__ == "__main__":
    fire.Fire(main)