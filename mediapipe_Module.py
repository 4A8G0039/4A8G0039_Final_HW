import cv2
import mediapipe as mp

class mediapipe_module():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_Hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) #設定手部偵測數值

        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_FaceMesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) #設定臉部偵測數值

        self.mp_pose = mp.solutions.pose
        self.mp_Pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) #設定軀幹偵測數值

        self.mp_drawing = mp.solutions.drawing_utils

    def mediapipe_calculate(self, frame, switch):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if switch[0]:
            hands_result = self.mp_Hands.process(imgRGB) #偵測手部
            if hands_result.multi_hand_landmarks: 
                for handLms in hands_result.multi_hand_landmarks: #讀取手部標記點
                    self.mp_drawing.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS, 
                                        self.mp_drawing.DrawingSpec(color=(255,0,255), thickness=2, circle_radius=3),
                                        self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)) #畫出手部標記點

        if switch[1]:
            face_mesh_result = self.mp_FaceMesh.process(imgRGB) #偵測臉部
            if face_mesh_result.multi_face_landmarks:
                for face_mesh_Lms in face_mesh_result.multi_face_landmarks: #讀取臉部標記點
                    self.mp_drawing.draw_landmarks(frame, face_mesh_Lms, self.mp_face_mesh.FACEMESH_CONTOURS, 
                                        self.mp_drawing.DrawingSpec(color=(0,255,200), thickness=1, circle_radius=1),
                                        self.mp_drawing.DrawingSpec(color=(255,255,255), thickness=1, circle_radius=1)) #畫出臉部標記點

        if switch[2]:
            Pose_result = self.mp_Pose.process(imgRGB) #偵測軀幹
            self.mp_drawing.draw_landmarks(frame, Pose_result.pose_landmarks, self.mp_pose.POSE_CONNECTIONS, 
                                        self.mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=3),
                                        self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=2)) #畫出軀幹標記點
        return frame