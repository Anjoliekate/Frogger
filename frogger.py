import pygame
import froggerlib

# this example game draws 3 concentric circles on top of a single color background
# the circles move down every time frame
# the user can control the circles by:
# - clicking the left mouse button to relocate them
# - holding the UP key to move them up
# - pressing the A key to move them to the left of the window
# - holding the A key to gradually move them to the right
class Frogger:


    def __init__( self, width, height, lane_size ): 
         self.mWidth = width 
         self.mHeight = height
         self.mLaneSize = lane_size
         self.mHalfGap = (lane_size - 40)/2
         self.mLaneCurr = 11
         self.mFrog = froggerlib.frog.Frog(self.mWidth/2, (self.mLaneCurr * self.mLaneSize + self.mHalfGap), 40, 40, self.mWidth/2, (self.mLaneCurr * self.mLaneSize + self.mHalfGap), 20, 50, 50 )
         
         self.mStage1 = froggerlib.stage.Stage(0, self.mLaneCurr * self.mLaneSize, self.mWidth, self.mLaneSize)
         
         self.mDodgeable = []
         self.mRoadLanes = []
         self.mWaterLanes = []
         self.mRideable = []
         
         self.mLaneCurr -= 1
         
         self.create_road_lane(3, 3, False, 60, 60, (255, 0, 0), froggerlib.Car)
         self.create_road_lane(2, 2, True, False, 80, (255, 0, 0), froggerlib.Truck)
         self.create_road_lane(2, 6, False, False, 60, (255, 0, 0), froggerlib.Dozer)
         self.create_road_lane(2, 4, False, 60, 60, (255, 0, 0), froggerlib.Car)
         
         self.mLaneCurr -= 2
         
         self.create_water_lane(3, 1, False, False, 120, (255, 150, 0), froggerlib.Log)
         self.create_water_lane(2, 2,True, True, 240, (255, 150, 0), froggerlib.Log)
         self.create_water_lane(3, 4, False, True, 50, (78, 157, 20), froggerlib.Turtle)
         self.create_water_lane(2, 3, True, True, 240, (255, 150, 0), froggerlib.Log)
         
         self.mLaneTreaders = self.mRideable + self.mDodgeable
         
         self.mHomes = []
         for i in range(4):
             self.mHomes.append(froggerlib.Home(i*200+100, 0, 100, 50))
             
         self.mGrasses = []
         for i in range(4):
             self.mGrasses.append(froggerlib.Grass(i*200, 0 , 100, 50))
             
         
         
         self.mGameOver = False
         return
         
         
    def create_lane(self, lane, num_objects, speed, direction, clumped, objects, width, color, lane_init, obj_init):
        created_lane = lane_init(0, lane*self.mLaneSize, self.mWidth, self.mLaneSize)
        w, h, y = width, 40, lane*self.mLaneSize+self.mHalfGap
        desired_x = None
        if direction:
            desired_x = self.mWidth + w
        else:
            desired_x = -w
            
        for i in range(num_objects):
            if clumped:
                x = self.mWidth - ((w+clumped)*i)
            else:
                x = self.mWidth - w - i*self.mWidth / num_objects
                
            obj = obj_init(x, y, w, h, desired_x, y , speed)
            obj.color = color
            objects.append(obj)
        return created_lane
    
    def create_water_lane(self, num_objects, speed, direction, clumped, width, color, obj_init):
        self.mWaterLanes.append(self.create_lane(self.mLaneCurr, num_objects, speed, direction, clumped, self.mRideable, width, color, froggerlib.water.Water, obj_init))
        self.mLaneCurr -= 1
        
 
    def create_road_lane(self, num_objects, speed, direction, clumped, width, color, obj_init):
        self.mRoadLanes.append(self.create_lane(self.mLaneCurr, num_objects, speed, direction, clumped, self.mDodgeable, width, color, froggerlib.road.Road, obj_init))
        self.mLaneCurr -= 1
        
   
    
    
    def evolve( self, dt ): 
         if self.mGameOver:#(first check that you do each frame) 
             return
            
         self.mFrog.move()
         if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
             self.mGameOver = True
             
         for lane_treaders in self.mLaneTreaders:
             lane_treaders.move()
             if lane_treaders.atDesiredLocation():
                 if lane_treaders.getDesiredX() <= 0:
                     lane_treaders.setX(self.mWidth + 1)
                 else:
                     lane_treaders.setX(-lane_treaders.getWidth())
                     
         for road_item in self.mDodgeable:
            if road_item.hits(self.mFrog):
                self.mGameOver = True
                
         for water_item in self.mRideable:
            water_item.supports(self.mFrog)
            
         for lane in self.mWaterLanes:
            if (lane.hits(self.mFrog)):
                self.mGameOver = True
                 
         for grass in self.mGrasses:
            if grass.hits( self.mFrog ):
                self.mGameOver = True
                 
         for home in self.mHomes:
            if home.hits(self.mFrog):
                self.mFrog.setX(self.mWidth/2)
                self.mFrog.setDesiredX(self.mWidth/2)
                self.mFrog.setY(11 * self.mLaneSize + self.mHalfGap)
                self.mFrog.setDesiredY(11 * self.mLaneSize + self.mHalfGap)
                
        
            
    def draw_rect(self, surface, locatable, color):
        rect = pygame.Rect(int(locatable.getX()), int(locatable.getY()), int(locatable.getWidth()), int(locatable.getHeight()))
        pygame.draw.rect(surface, color, rect, 0)
        
            
    def draw( self, surface ):
        #Rectangle to draw on entire game screen
        rect = pygame.Rect(int(0), int(0), int(self.mWidth), int(self.mHeight))
        pygame.draw.rect(surface, (171, 106, 171), rect)
        self.draw_rect(surface, self.mStage1, (189, 235, 52))
         
         #Stage one
        
        
        for lane in self.mRoadLanes:
            self.draw_rect(surface, lane, (50, 50, 50))
            
        for lane in self.mWaterLanes:
            self.draw_rect(surface, lane, (50, 50, 255))
            
        for lane_treaders in self.mLaneTreaders:
            self.draw_rect(surface, lane_treaders, lane_treaders.color)
            
        for home in self.mHomes:
            self.draw_rect(surface, home, (50, 150, 150))
            
            
        for grass in self.mGrasses:
            self.draw_rect(surface, grass, (50, 150, 50))
            
            
        self.draw_rect(surface, self.mFrog, (15, 150, 11))
        
        
        return
        
    def actOnPressUP( self ): 
        self.mFrog.up() 
        return
    def actOnPressDOWN( self ): 
        self.mFrog.down() 
        return
    def actOnPressLEFT( self ): 
        self.mFrog.left() 
        return
    def actOnPressRIGHT( self ): 
        self.mFrog.right() 
        return 
