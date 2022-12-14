# ProjectPygame

### 1. 시작화면 구현
- 시작 화면에서 스페이스 누를 시 파이게임 창이 종료 되었다가 새로운 창이 나타남
<img src="https://user-images.githubusercontent.com/107173046/200728183-f3d1c6fb-4ab7-4ce4-802d-312bbcfb3755.png" width="500">

<br>

---

<br>
  
### 2. 맵 구현
- 화살표 좌우방향으로 움직임 구현. 지정한 x 좌표에서 스페이스 누를 시 다음 스테이지로 넘어감. 

<img src="https://user-images.githubusercontent.com/107173046/200728282-bba75d8e-9aea-4f32-9d84-fa1c7fba85dd.png" width="500">

<img src="https://user-images.githubusercontent.com/107173046/200728473-95d1819a-fd0e-46f7-a5d1-7157f90f6244.png" width="500">

<br>

---

<br>

### 3. 1번째 스테이지 구현
- 공룡게임(구글링 참조)
- 반복문 한 번 돌 때마다 그림 바뀜, 달리는 모션
- 시간을 지정하여 그 시간이 지난 후에 자동으로 게임 종료
- 장애물의 렉터값, 캐릭터릐 렉터값을 구해 둘의 충돌이 일어난 경우 반복문 False

<img src="https://user-images.githubusercontent.com/107173046/200728405-0ab47422-e7b8-420c-b673-957e7c2c2137.png" width="500">

<br>

---

<br>

### 4. 2번째 스테이지 구현
- 버블슈터(유튜브 참조)
- 정해둔 횟수가 넘어간 경우 위에서 벽이 내려옴
- 지정한 y 좌표 아래까지 버블이 내려온 경우 반복문 False
- 남아있는 버블의 색깔 중에서 랜덤으로 쏠 버블 색 지정
- 같은 색의 버블 3개 이상이 모이면 버블 삭제

<img src="https://user-images.githubusercontent.com/107173046/200728425-8aa992ad-8166-490a-917f-8222b4fcc758.png" width="500">

<br>

---

<br>

### 5. 3번째 스테이지 구현
- 몬스터슈팅(유튜브 참조)
- 벽에 부딪히면 다시 돌아옴. 크기별로 속도, 높이 지정
- 캐릭터의 렉터값과 몬스터의 렉터값이 충돌하면 반복문 False
- 무기의 렉터값이 몬스터의 렉터값과 충돌하면 몬스터가 작은 크기로 나누어짐. 마지막 크기의 몬스터는 삭제
- 시간 제한
- 정해둔 시간마다 그림이 바뀜 > 걷는 모션
- 좌, 우, 스페이스 버튼 별로 캐릭터의 모션이 바뀜

<img src="https://user-images.githubusercontent.com/107173046/200728507-3f341e30-ba6a-490a-a176-0c5433fbc864.png" width="500">

<br>

---

### 6. 엔딩 구현
- 영화관 쿠키, 엔딩 장면처럼 구현
- 정해진 시간마다 그림이 바뀜
- 배경의 y 좌표 속도 지정, 반복문 한 번 돌 때마다 y 좌표가 줄어들어 화면상으론 그림이 위로 올라감

<img src="https://user-images.githubusercontent.com/107173046/200728519-d8498a40-635e-4c6e-b0b7-718a7dbd8309.png" width="500">

<img src="https://user-images.githubusercontent.com/107173046/200728538-2673395d-f1b5-4afd-9f5b-9b1ec099e57e.png" width="500">


<br>

---

<br>

### 7. 스토리라인 & 엔딩크레딧
- 용사가 공주를 구하러 가는 고전~ 느낌의 게임
- 시작, 각 스테이지의 끝, 엔딩 부분에 스토리가 들어감
- 마지막엔 첫 스테이지의 나온 장애물과 캐릭터가 등장하여 귀엽게 마무리~

<img src="https://user-images.githubusercontent.com/107173046/200728232-1ca101b2-b4c7-41aa-8b81-294a78820e5d.png" width="500">

<img src="https://user-images.githubusercontent.com/107173046/200728307-f5f9e2f5-7c77-473b-affe-9d87cb8f6cc2.png" width="500">

<img src="https://user-images.githubusercontent.com/107173046/200728651-9d2eefc4-e1e4-4a0f-b3a7-e079c327969b.png" width="500">

<img src="https://user-images.githubusercontent.com/107173046/200728679-e871097c-f311-4d26-933b-450dcb72f35c.png" width="500">
