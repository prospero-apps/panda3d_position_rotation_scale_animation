# file name: pm1B10.py
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.interval.IntervalGlobal import Sequence, Parallel
import simplepbr

class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.setBackgroundColor(.53, .81, .92)
        simplepbr.init()       
        props = WindowProperties()
        props.setSize(1200, 675)
        base.win.requestProperties(props)

        self.ufo = loader.loadModel('UFO/UFO.gltf')
        self.ufo.setPos(0, 50, 5)
        self.ufo.reparentTo(render)   

        self.terrain = loader.loadModel('terrain/terrain.gltf')
        self.terrain.setPos(0, 50, -12)
        self.terrain.reparentTo(render) 

        # the single intervals
        posInterval1 = self.ufo.posInterval(3, (10, 50, 5)) 
        posInterval2 = self.ufo.posInterval(2, (0, 20, 1))
        hprInterval1 = self.ufo.hprInterval(5, (0, 45, 0))  
        posInterval3 = self.ufo.posInterval(1, (2, 20, 1))
        hprInterval2 = self.ufo.hprInterval(1, (0, 15, 15))   
        posInterval4 = self.ufo.posInterval(1, (0, 20, -3))
        hprInterval3 = self.ufo.hprInterval(1, (0, -15, -15))   
        hprInterval4 = self.ufo.hprInterval(2, (360, 0, 0))
        hprInterval5 = self.ufo.hprInterval(1, (720, 0, 0))
        posInterval5 = self.ufo.posInterval(1, (150, 500, 30))
        posInterval6 = self.ufo.posInterval(.25, (300, 500, 30))

        # the nested sequence
        Sequence(Sequence(posInterval1, posInterval2, hprInterval1), 
                 Sequence(
                     Parallel(posInterval3, hprInterval2), 
                     Parallel(posInterval4, hprInterval3)), 
                 hprInterval4, 
                 hprInterval5, 
                 posInterval5, 
                 posInterval6).start()

app = TestApp()
app.run()
