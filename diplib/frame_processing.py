import cv2
import numpy as np

def frames_rgb_to_hsv(self, frames):
    g_frames = []
    for frame in frames:
        g_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
    return np.array(g_frames, dtype='uint8')

def frames_hsv_to_rgb(self, frames):
    g_frames = []
    for frame in frames:
        g_frames.append(cv2.cvtColor(frame, cv2.COLOR_HSV2BGR))
    return np.array(g_frames, dtype='uint8')

def find_lowest_point(self, prev, next, x, y, w, z, radius):
    min_x, min_y = w, z
    try:
        residual = np.sum(np.multiply(next[min_x-1:min_x+2, min_y-1:min_y+2]-prev[x-1:x+2, y-1:y+2],next[min_x-1:min_x+2, min_y-1:min_y+2]-prev[x-1:x+2, y-1:y+2]))
        for (cx, cy) in [(w-radius, z+radius),(w, z+radius),(w+radius, z+radius),(w-radius, y),(z+radius, y),(w-radius, z-radius),(w, z-radius),(w+radius, z-radius)]:
            try:
                new_residual = np.sum(np.multiply(next[cx-1:cx+2, cy-1:cy+2]-prev[x-1:x+2, y-1:y+2],next[cx-1:cx+2, cy-1:cy+2]-prev[x-1:x+2, y-1:y+2]))
                if new_residual < residual:
                    min_x, min_y = cx, cy
                    residual = new_residual
            except:
                pass
    except:
        pass
    return min_x, min_y

def three_step_search(self, frames, radius=4):
    color = np.random.randint(0,255,(200,3))
    lines = None  #추적 선을 그릴 이미지 저장 변수
    prev = None  # 이전 프레임 저장 변수
    
    new_frames = []
    for i in range(frames.shape[0]):
        img_draw = frames[i].copy()
        gray = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        if prev is None:
            prev = gray
            # 추적선 그릴 이미지를 프레임 크기에 맞게 생성
            lines = np.zeros_like(frames[i])
            # 추적 시작을 위한 코너 검출
            prevPt = cv2.goodFeaturesToTrack(prev, 200, 0.01, 10)
        else:
            next = gray
            for j, point in enumerate(prevPt):
                a, b = int(point[0, 0].copy()), int(point[0, 1].copy())
                c, d = self.find_lowest_point(prev, next, a, b, a, b, radius)
                c, d = self.find_lowest_point(prev, next, a, b, c, d, int(radius/2))
                c, d = self.find_lowest_point(prev, next, a, b, c, d, int(radius/4))
                try:
                    # 이전 코너와 새로운 코너에 선그리기
                    cv2.line(lines, (int(a), int(b)), (int(c),int(d)), color[i].tolist(), 2)
                    # 새로운 코너에 점 그리기
                    cv2.circle(img_draw, (int(c),int(d)), 2, color[i].tolist(), -1)
                except:
                    pass
                prevPt[j, 0, 0], prevPt[j, 0, 1] = c, d
            # 누적된 추적 선을 출력 이미지에 합성
            img_draw = cv2.add(img_draw, lines)
            prev = next
        new_frames.append(img_draw)
    return np.array(new_frames, dtype='uint8')

def lucas_kanade(self, frames):
    # 추적 경로를 그리기 위한 랜덤 색상
    color = np.random.randint(0,255,(200,3))
    lines = None  #추적 선을 그릴 이미지 저장 변수
    prev = None  # 이전 프레임 저장 변수
    # calcOpticalFlowPyrLK 중지 요건 설정
    termcriteria =  (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
    new_frames = []
    for i in range(frames.shape[0]):
        img_draw = frames[i].copy()
        gray = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        if prev is None:
            prev = gray
            # 추적선 그릴 이미지를 프레임 크기에 맞게 생성
            lines = np.zeros_like(frames[i])
            # 추적 시작을 위한 코너 검출  ---①
            prevPt = cv2.goodFeaturesToTrack(prev, 200, 0.01, 10)
        else:
            next = gray
            # 옵티컬 플로우로 다음 프레임의 코너점  찾기 ---②
            nextPt, status, err = cv2.calcOpticalFlowPyrLK(prev, next, \
                                            prevPt, None, criteria=termcriteria)
            # 대응점이 있는 코너, 움직인 코너 선별 ---③
            prevMv = prevPt[status==1]
            nextMv = nextPt[status==1]
            for i,(p, n) in enumerate(zip(prevMv, nextMv)):
                px,py = p.ravel()
                nx,ny = n.ravel()
                # 이전 코너와 새로운 코너에 선그리기 ---④
                cv2.line(lines, (int(px), int(py)), (int(nx),int(ny)), color[i].tolist(), 2)
                # 새로운 코너에 점 그리기
                cv2.circle(img_draw, (int(nx),int(ny)), 2, color[i].tolist(), -1)
            # 누적된 추적 선을 출력 이미지에 합성 ---⑤
            img_draw = cv2.add(img_draw, lines)
            # 다음 프레임을 위한 프레임과 코너점 이월
            prev = next
            prevPt = nextMv.reshape(-1,1,2)
        new_frames.append(img_draw)
    return np.array(new_frames, dtype='uint8')

def gunar_farneback(self, frames):
    prev = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frames[0])
    hsv[...,1] = 255
    new_frames = []
    for i in range(frames.shape[0]):
        if i==0:
            pass
        else:
            next = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prev, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
            hsv[...,0] = ang*180/np.pi/2
            hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            new_frames.append(bgr)
            prev = next
    return np.array(new_frames, dtype='uint8')