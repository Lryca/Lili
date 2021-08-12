import discord
from discord.ext import commands
import os
import random
import time

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("낚시")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("MEOW")

    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.

        if message.author.bot and message.content == "리리한테 가봐요":
            channel = message.channel
            msg="오빠 나 건들지마."
            await channel.send(msg)
            return None
            
        if message.author.bot:
            return None
        
        # message.content = message의 내용
        if message.content == "리리야 안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "잘 부탁드려요냥"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "리리야 참치":
            channel = message.channel
            msg = "그.. 주시면 감사히받을게요냥"
            await channel.send(msg)
            return None

        if message.content == "리리야 사랑해":
            channel = message.channel
            msg = "네?! 저..저도 사랑합니다"
            await channel.send(msg)
            return None
        
        if message.content == "리리야 고고가 누구야?":
            channel = message.channel
            msg = "구제불능인 저희 오빠에요냥.. 좀 이상한 말 해도 참아주세요."
            await channel.send(msg)
            return None

        if message.content == "리리야 유유가 누구야?":
            channel =  message.channel
            msg="책을 좋아하는 남동생이에요냥 너무 활발해서 탈이에요."
            await channel.send(msg)
            return None 

        if message.content == "리리야 뭐해":
             channel = message.channel
             num=random.randint(1,3)
             if num==1 :
                 asw="장수풍뎅이에게 먹이를 주고 있어요."
                 await channel.send(asw)
                 return None
             if num==2 :
                 asw="잠자리채를 고치고 있어요."
                 await channel.send(asw)
                 return None
             if num==3 :
                 asw="낚시 줄을 갈고 있어요."
                 await channel.send(asw)
                 return None  
        
        if message.content == "리리야 낚시":
            channel = message.channel
            # Embed 메시지 구성
            fish_C=["올챙이","납줄개","빙어","붕어","미꾸라지","잉어","황어","은어","전갱이","농어","모래무지","넙치","틸라피아","도미","가자미","고등어","정어리","멸치","마리모","우럭","피라미","베스","쏠배감팽","꽃게","청어","갯민숭달팽이","미역","가리비","블루길","꽁치","송사리","불가사리","해파리","볼락","해마","낙지","망둥어","한치","누치","해삼","말미잘","갈치","까나리","달고기","쥐치","가재","동사리","놀래기","놀래미","삼치","뱅애돔"]
            fish_R=["금붕어","개구리","툭눈금붕어","연어","메기","오징어","문어","가시고기","클리오네","금강바리","자라","담셀","구피","네온테트라","닥터피쉬","레인보우피쉬","앵무조개","나비고기","블루탱","박스피쉬","장어","갑오징어","디스커스","베타","리본장어","새우","옐로우퍼치","무지개송어","방어","성게","가시복","깃대돔","천사어","키싱구라미","임연수어","옐로탱","코리도라스","그루퍼","쉬리","돌고기","비파","도루묵","고비","유니콘피쉬","날새기","두꺼비"]
            fish_E=["산천어","열목어","비단잉어","돌돔","피라니아","흰동가리","가오리","늑대거북","칠성장어","아귀","만새기","날치","청새치","날개다랑어","다랑어","곰치","바다거북","아델리펭귄","마젤란펭귄","가아","가물치","전기뱀장어","우파루파","빨판상어","투구게","강꼬치고기","맨티스쉬림프","잉어킹","물개","복어","수달","해룡","대게","바다뱀","플라워혼","통안어","킹크랩","랍스터","가든일","홍어","우무문어"]
            fish_S=["개복치","산갈치","톱상어","피라루크","아로와나","귀상어","엔드리캐리","돌고래","범고래","하프물범","황제펭귄","나폴레옹피쉬","북극곰","블로브피쉬","듀공","바다표범","일각고래","벨루가","니모","청상아리","철갑상어","오리너구리","바다코끼리","장수거북","바다돼지","향유고래"]
            fish_L=["배럴아이","실러캔스","황금연어","이무기","흰긴수염고래","백상아리","고래상어","분홍돌고래","폐어","이크티오사우루스","크라켄","악어","인면어","수영하던 고고","메갈로돈","뽀로로","만타가오리","네시","틱타알릭"]
            fish_T=["쓰레기","신문지","유목","그물망","고고의 박스","깡통","타이어","스티로폼","패트병","비닐봉지","리리의 털실","유유의 생선뼈","과일껍질","달걀껍질","녹슨부품","돌맹이","녹지 않은 얼음","수수깡","비닐우산"]
            n=random.randint(1,100)
            channel = message.channel
            embed = discord.Embed(title="<낚시를 시작할게요!>", description="과연 뭐가 잡할까?", color=0x58D3F7)
            await channel.send(embed=embed)
            time.sleep(3)
            #1성 물고기 총 51마리
            if n>=1 and n<=30:
                nm=random.randint(0,50)
                embed = discord.Embed(title="<낚시 결과>", description="★무언가 잡힌 것 같아요 냥!★", color=0x58D3F7)
                embed.add_field(name="==========================", value="결과", inline=True)
                embed.add_field(name=fish_C[nm], value="등급 ★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)
            #2성 물고기 총 46마리
            if n>=31 and n<=60:
                nm=random.randint(0,45)
                embed = discord.Embed(title="<낚시 결과>", description="★오오 멋진 물고기에요 냥★", color=0x58D3F7)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=fish_R[nm], value="등급 ★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)
            #3성 물고기 총 40마리
            if n>=61 and n<=80:
                nm=random.randint(0,39)
                embed = discord.Embed(title="<낚시 결과>", description="★좀처럼 볼 수 없는 물고기에요 냥!★", color=0x58D3F7)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=fish_E[nm], value="등급 ★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)
            #4성 물고기 총 27마리d
            if n>=81 and n<=90:
                nm=random.randint(0,26)
                embed = discord.Embed(title="<낚시 결과>", description="★이런 물고기는 처음봤어요 냥!★", color=0x58D3F7)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=fish_S[nm], value="등급 ★★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)
            #5성 물고기 총 19마리
            if n>=91 and n<=92:
                nm=random.randint(0,18)
                embed = discord.Embed(title="<낚시 결과>", description="★이런 물고기는 처음봤어요 냥!★", color=0x58D3F7)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=fish_L[nm], value="등급 ★★★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)
            #쓰레기 총 18개
            if n>=93 and n<=97:
                nm=random.randint(0,17)
                embed = discord.Embed(title="<낚시 결과>", description="아 이건.. 안타깝군요..", color=0x58D3F7)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=fish_T[nm], value="등급 쓰레기", inline=False)
                embed.set_footer(text="다음엔 더 잘 할 수 있을거에요.")
                await channel.send(embed=embed)
            #낚시 실패
            if n>=98 and n<=100:
                nm=random.randint(1,4)
                if nm==1:
                    embed = discord.Embed(title="<낡은 낚시줄>", description="아..낚시줄이 끊어졌어요...", color=0x58D3F7)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==2:
                    embed = discord.Embed(title="<날쎈 물고기>", description="물고기가 미끼를 먹고 도망갔어요..", color=0x58D3F7)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==3:
                    embed = discord.Embed(title="<부러진 낚시대>", description="힘조절을 잘못했나봐요..", color=0x58D3F7)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==4:
                    embed = discord.Embed(title="<잘못된 자리선정>", description="아무리 기다려도 물고기가 걸리지 않아요...", color=0x58D3F7)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                    
        if message.content == "리리야 잠자리채":
            channel = message.channel

            # Embed 메시지 구성
            Bug_C=["배추흰나비","모기","바퀴벌레","그리마","날파리","등에","진딧물","벼룩","물벼룩","진드기","구더기","굼벵이","책벌레","곱등이","노랑나비","파리","매미허물","무당벌레","갯강구","민달팽이","지네","공벌레","쥐며느리","지렁이"]
            Bug_R=["소금쟁이","물방개","호랑나비","사마귀","고추잠자리","왕잠자리","애매미","참매미","오색나비","부르키아나나비","길앞잡이","풍뎅이","꿀벌"]
            Bug_E=["호랑거미","긴수염대벌레","하늘소","물장군","보석풍뎅이","장수풍뎅이","사슴벌레", "꽃무지", "누에나방", "비단벌레"]
            Bug_S=["장수말벌","코카서스왕장수풍뎅이","알렉산드라제비나비","가라파톱사슴벌레","코끼리장수풍뎅이","뮤엘러리사슴벌레","엘라푸스가위사슴벌레","산누에나방","장수잠자리"]
            Bug_L=["운석","별똥별","페어리","헤라클레스 장수풍뎅이","황금 사슴벌레","와이번","드래곤","황제전갈","타란툴라","페가수스","세인트헬레나집게벌레","기간티아","유니콘"]
            Bug_T=["리리의 드론", "고고의 민들레씨", "유유의 헛된 꿈", "비행기", "우주정거장", "조화", "장수풍뎅이 모형","누군가의 소망","연"]
            n=random.randint(1,100)
            channel = message.channel
            embed = discord.Embed(title="<잠자리채를 휘두를게요!>", description="살금살금 다가가는 중이에요...", color=0x00FF00)
            await channel.send(embed=embed)
            time.sleep(3)
            #1성 곤충 총 23마리
            if n>=1 and n<=30:
                nm=random.randint(0,22)
                embed = discord.Embed(title="<채집 결과>", description="★평범한 결과에요★", color=0x00FF00)
                embed.add_field(name="==========================", value="결과", inline=True)
                embed.add_field(name=Bug_C[nm], value="등급 ★", inline=False)
                embed.set_footer(text="다음엔 더 노력해봐요")
                await channel.send(embed=embed)

            #2성 곤충 총 13마리
            if n>=31 and n<=60:
                nm=random.randint(0,12)
                embed = discord.Embed(title="<채집 결과>", description="★오오 멋진 곤충이에요 냥★", color=0x00FF00)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=Bug_R[nm], value="등급 ★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)

            #3성 곤충 총 10마리
            if n>=61 and n<=80:
                nm=random.randint(0,9)
                embed = discord.Embed(title="<채집 결과>", description="★희귀한 곤충을 잡았어요!★", color=0x00FF00)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=Bug_E[nm], value="등급 ★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)

            #4성 곤충 총 9마리
            if n>=81 and n<=90:
                nm=random.randint(0,8)
                embed = discord.Embed(title="<채집 결과>", description="★팔면 돈이 될지도 모르겠는데요?★", color=0x00FF00)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=Bug_S[nm], value="등급 ★★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)

            #5성 곤충 총 13마리
            if n>=91 and n<=92:
                nm=random.randint(0,12)
                embed = discord.Embed(title="<채집 결과>", description="★이런 곤충은 처음봤어요 냥!★", color=0x00FF00)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=Bug_L[nm], value="등급 ★★★★★", inline=False)
                embed.set_footer(text="다음엔 뭐가 잡힐까요냥?")
                await channel.send(embed=embed)

            #쓰레기 총 9개
            if n>=93 and n<=97:
                nm=random.randint(0,8)
                embed = discord.Embed(title="<채집 결과>", description="아 이건.. 안타깝군요..", color=0x00FF00)
                embed.add_field(name="=====================", value="결과", inline=True)
                embed.add_field(name=Bug_T[nm], value="등급 쓰레기", inline=False)
                embed.set_footer(text="다음엔 더 잘 할 수 있을거에요.")
                await channel.send(embed=embed)

            if n>=98 and n<=100:
                nm=random.randint(1,5)
                if nm==1:
                    embed = discord.Embed(title="<낡은 잠자리채>", description="아..잠자리채가 부서졌어요...", color=0x00FF00)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==2:
                    embed = discord.Embed(title="<날쎈 벌레>", description="저를 눈치챈것 같아요...", color=0x00FF00)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==3:
                    embed = discord.Embed(title="<넘어진 리리>", description="아야.. 넘어졌어요...", color=0x00FF00)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==4:
                    embed = discord.Embed(title="<유유의 방해>", description="이게 미쳤나", color=0x00FF00)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)
                if nm==5:
                    embed = discord.Embed(title="<고고의 방해>", description="장난쳐??", color=0x00FF00)
                    embed.set_footer(text="우리 다시 해봐요.")
                    await channel.send(embed=embed)

    


if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(os.environ['token'])