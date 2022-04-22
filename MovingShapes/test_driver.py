## @file test_All.py
#  @author Mathew Petronilho
#  @brief Testing of CircleT.py, TriangleT.py, Bodyt.py and Scene.py
#  @date February 8, 2021

import math
from scipy import integrate
from BodyT import *
from CircleT import *
from TriangleT import *
from Scene import *

import pytest


# tests methods from CircleT
class TestCircleT:

    def setup_method(self, method):
        self.circle1 = CircleT(2, 3, 5, 10)
        self.circle2 = CircleT(-3, -5, 4, 12)
        self.circle3 = CircleT(0, 0, 2, 6)
        self.circle4 = CircleT(6.000002, -3.99998, 5.23234, 8.000234)

    def teardown_method(self, method):
        self.circle1 = None
        self.circle2 = None
        self.circle3 = None
        self.circle4 = None

    # testing of constructor
    def test_constructor_1(self):
        with pytest.raises(ValueError):
            CircleT(2, 3, 0, 4)

    def test_constructor_2(self):
        with pytest.raises(ValueError):
            CircleT(2, 3, 3, -2)

    # testing of cm_x
    def test_cmx_1(self):
        assert self.circle1.cm_x() == 2

    def test_cmx_2(self):
        assert self.circle2.cm_x() == -3

    def test_cmx_3(self):
        assert self.circle3.cm_x() == 0

    def test_cmx_4(self):
        assert self.circle4.cm_x() == pytest.approx(6, abs=1e-3)

    # testing of cm_y
    def test_cmy_1(self):
        assert self.circle1.cm_y() == 3

    def test_cmy_2(self):
        assert self.circle2.cm_y() == -5

    def test_cmy_3(self):
        assert self.circle3.cm_y() == 0

    def test_cmy_4(self):
        assert self.circle4.cm_y() == pytest.approx(-4, abs=1e-3)

    # testing of mass
    def test_mass_1(self):
        assert self.circle1.mass() == 10

    def test_mass_2(self):
        assert self.circle2.mass() == 12

    def test_mass_3(self):
        assert self.circle3.mass() == 6

    def test_mass_4(self):
        assert self.circle4.mass() == pytest.approx(8, abs=1e-3)

    # testing of minert
    def test_minert_1(self):
        assert self.circle1.m_inert() == pytest.approx(125, abs=1e-3)

    def test_minert_2(self):
        assert self.circle2.m_inert() == pytest.approx(96, abs=1e-3)

    def test_minert_3(self):
        assert self.circle3.m_inert() == pytest.approx(12, abs=1e-3)

    def test_minert_4(self):
        assert self.circle4.m_inert() == pytest.approx(109, abs=0.6)


# tests methods from TriangleT
class TestTriangleT:

    def setup_method(self, method):
        self.tri1 = TriangleT(2, 3, 5, 10)
        self.tri2 = TriangleT(-3, -5, 4, 12)
        self.tri3 = TriangleT(0, 0, 2, 6)
        self.tri4 = TriangleT(6.000002, -3.99998, 5.00004, 8.000234)

    def teardown_method(self, method):
        self.tri1 = None
        self.tri2 = None
        self.tri3 = None
        self.tri4 = None

    # testing of constructor
    def test_constructor_1(self):
        with pytest.raises(ValueError):
            TriangleT(2, 3, 0, 4)

    def test_constructor_2(self):
        with pytest.raises(ValueError):
            TriangleT(2, 3, 3, -2)

    # testing of cm_x
    def test_cmx_1(self):
        assert self.tri1.cm_x() == 2

    def test_cmx_2(self):
        assert self.tri2.cm_x() == -3

    def test_cmx_3(self):
        assert self.tri3.cm_x() == 0

    def test_cmx_4(self):
        assert self.tri4.cm_x() == pytest.approx(6, abs=1e-3)

    # testing of cm_y
    def test_cmy_1(self):
        assert self.tri1.cm_y() == 3

    def test_cmy_2(self):
        assert self.tri2.cm_y() == -5

    def test_cmy_3(self):
        assert self.tri3.cm_y() == 0

    def test_cmy_4(self):
        assert self.tri4.cm_y() == pytest.approx(-4, abs=1e-3)

    # testing of mass
    def test_mass_1(self):
        assert self.tri1.mass() == 10

    def test_mass_2(self):
        assert self.tri2.mass() == 12

    def test_mass_3(self):
        assert self.tri3.mass() == 6

    def test_mass_4(self):
        assert self.tri4.mass() == pytest.approx(8, abs=1e-3)

    # testing of minert
    def test_minert_1(self):
        assert self.tri1.m_inert() == pytest.approx(20.8, abs=0.1)

    def test_minert_2(self):
        assert self.tri2.m_inert() == pytest.approx(16, abs=1e-3)

    def test_minert_3(self):
        assert self.tri3.m_inert() == pytest.approx(2, abs=1e-3)

    def test_minert_4(self):
        assert self.tri4.m_inert() == pytest.approx(16.6, abs=0.1)


# tests methods from BodyT
class TestBodyT:

    def setup_method(self, method):
        self.body1 = BodyT([2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [11, 12, 13, 14, 15])
        self.body2 = BodyT([-2, -3, -3], [-4, -6, -2], [3, 6, 9])
        self.body3 = BodyT([0, 0, 0, 0], [0, 0, 0, 0], [3, 60, 4, 8])
        self.body4 = BodyT([-3.5, 6.05, -3.0001], [4.8, -2.2, -7.3], [3.2, 5.6, 9.99])

    def teardown_method(self, method):
        self.body1 = None
        self.body2 = None
        self.body3 = None
        self.body4 = None

    # testing of constructor
    def test_constructor_1(self):
        with pytest.raises(ValueError):
            BodyT([1, 2, 3], [4, 5, 5], [5, 6, 7, 8])

    def test_constructor_2(self):
        with pytest.raises(ValueError):
            BodyT([1, 23, 4], [5, 6, 3], [0, -5, 7])

    # testing of cm_x
    def test_cmx_1(self):
        assert self.body1.cm_x() == pytest.approx(4.15, abs=0.01)

    def test_cmx_2(self):
        assert self.body2.cm_x() == pytest.approx(-2.83, abs=0.01)

    def test_cmx_3(self):
        assert self.body3.cm_x() == 0

    def test_cmx_4(self):
        assert self.body4.cm_x() == pytest.approx(-0.388, abs=1e-3)

    # testing of cm_y
    def test_cmy_1(self):
        assert self.body1.cm_y() == pytest.approx(9.15, abs=0.01)

    def test_cmy_2(self):
        assert self.body2.cm_y() == pytest.approx(-3.6666, abs=0.0001)

    def test_cmy_3(self):
        assert self.body3.cm_y() == 0

    def test_cmy_4(self):
        assert self.body4.cm_y() == pytest.approx(-3.72, abs=0.01)

    # testing of mass
    def test_mass_1(self):
        assert self.body1.mass() == pytest.approx(65, abs=1e-6)

    def test_mass_2(self):
        assert self.body2.mass() == pytest.approx(18, abs=1e-6)

    def test_mass_3(self):
        assert self.body3.mass() == pytest.approx(75, abs=1e-6)

    def test_mass_4(self):
        assert self.body4.mass() == pytest.approx(18.8, abs=0.02)

    # testing of minert
    def test_minert_1(self):
        assert self.body1.m_inert() == pytest.approx(256.92, abs=0.01)

    def test_minert_2(self):
        assert self.body2.m_inert() == pytest.approx(60.5, abs=1e-3)

    def test_minert_3(self):
        assert self.body3.m_inert() == pytest.approx(0, abs=1e-6)

    def test_minert_4(self):
        assert self.body4.m_inert() == pytest.approx(704.52, abs=0.01)


# tests methods from Scene
class TestScene:

    def setup_method(self, method):
        # falling under force of gravity
        self.scene1 = Scene(CircleT(2, 3, 5, 10), lambda x: 0, lambda x: -9.8 * x, 0, 0)
        vx = 10 * math.cos(math.pi / 4)
        vy = 10 * math.sin(math.pi / 4)
        # falling with projectile motion
        self.scene2 = Scene(TriangleT(0, 0, 2, 6), lambda x: 0, lambda x: -9.8 * x, vx, vy)
        # test case with no force
        test = BodyT([-3.5, 6.05, -3.0001], [4.8, -2.2, -7.3], [3.2, 5.6, 9.99])
        self.scene3 = Scene(test, lambda x: 0, lambda x: 0, 0, 0)

    def teardown_method(self, method):
        self.scene1 = None
        self.scene2 = None
        self.scene3 = None

    # testing of get shape
    def test_shape_1(self):
        s1 = self.scene1.get_shape()
        s2 = CircleT(2, 3, 5, 10)
        cm = s1.cm_x() == s2.cm_x() and s1.cm_y() == s2.cm_y()
        mass = s1.mass() == s2.mass()
        inert = s1.m_inert() == s2.m_inert()
        assert cm and mass and inert

    def test_shape_2(self):
        s1 = self.scene2.get_shape()
        s2 = TriangleT(0, 0, 2, 6)
        cm = s1.cm_x() == s2.cm_x() and s1.cm_y() == s2.cm_y()
        mass = s1.mass() == s2.mass()
        inert = s1.m_inert() == s2.m_inert()
        assert cm and mass and inert

    def test_shape_3(self):
        test = BodyT([-3.5, 6.05, -3.0001], [4.8, -2.2, -7.3], [3.2, 5.6, 9.99])
        s1 = self.scene3.get_shape()
        cm = s1.cm_x() == test.cm_x() and s1.cm_y() == test.cm_y()
        mass = s1.mass() == test.mass()
        inert = s1.m_inert() == test.m_inert()
        assert cm and mass and inert

    # testing of get initial velocity
    def test_init_vel_1(self):
        assert self.scene1.get_init_velo() == (0, 0)

    def test_init_vel_2(self):
        x = pytest.approx(10 / math.sqrt(2), abs=0.001)
        assert self.scene2.get_init_velo() == (x, x)

    def test_init_vel_3(self):
        assert self.scene3.get_init_velo() == (0, 0)

    def test_set_shape_1(self):
        # switching shape
        self.scene1.set_shape(TriangleT(2, 3, 5, 10))
        s1 = self.scene1.get_shape()
        s2 = TriangleT(2, 3, 5, 10)
        cm = s1.cm_x() == s2.cm_x() and s1.cm_y() == s2.cm_y()
        mass = s1.mass() == s2.mass()
        inert = s1.m_inert() == s2.m_inert()
        assert cm and mass and inert

    def test_set_shape_2(self):
        # same shape, diff parameters
        self.scene1.set_shape(TriangleT(4, 5, 6, 7))
        s1 = self.scene1.get_shape()
        s2 = TriangleT(4, 5, 6, 7)
        cm = s1.cm_x() == s2.cm_x() and s1.cm_y() == s2.cm_y()
        mass = s1.mass() == s2.mass()
        inert = s1.m_inert() == s2.m_inert()
        assert cm and mass and inert
        self.scene1.set_shape(CircleT(2, 3, 5, 10))

    def test_set_shape_3(self):
        # same shape exactly
        test = BodyT([-3.5, 6.05, -3.0001], [4.8, -2.2, -7.3], [3.2, 5.6, 9.99])
        self.scene3.set_shape(test)
        s1 = self.scene3.get_shape()
        cm = s1.cm_x() == test.cm_x() and s1.cm_y() == test.cm_y()
        mass = s1.mass() == test.mass()
        inert = s1.m_inert() == test.m_inert()
        assert cm and mass and inert

    # testing for set velocity
    def test_set_velo_1(self):
        self.scene1.set_init_velo(-4, 5)
        assert self.scene1.get_init_velo() == (-4, 5)

    def test_set_velo_2(self):
        self.scene1.set_init_velo(332, 43)
        assert self.scene1.get_init_velo() == (332, 43)

    def test_set_velo_3(self):
        self.scene1.set_init_velo(0, 0)
        assert self.scene1.get_init_velo() == (0, 0)

    # testing sim
    def test_sim_1(self):
        t, s = self.scene1.sim(10, 10)
        t2 = [(i * 10) / 9 for i in range(0, 10)]
        t3 = [t2[i] - t[i] for i in range(len(t))]
        max1 = max(t3, key=abs) / max(t, key=abs)

        lst = [2, 3, 0, 0]

        def func(w, t):
            return [w[2], w[3], 0, (-9.8 * t) / 10]
        s2 = integrate.odeint(func, lst, t)
        s3 = []
        s4 = []
        for i in range(len(s2)):
            for j in range(0, 4):
                s3.append(s2[i][j])
                s4.append(s[i][j])
        s5 = [s3[i] - s4[i] for i in range(len(s4))]
        max2 = max(s5, key=abs) / max(s4, key=abs)
        assert (abs(max1) < 0.001)
        assert (abs(max2) < 0.001)

    def test_sim_2(self):
        t, s = self.scene2.sim(10, 10)
        t2 = [(i * 10) / 9 for i in range(0, 10)]
        t3 = [t2[i] - t[i] for i in range(len(t))]
        max1 = max(t3, key=abs) / max(t, key=abs)

        vx = 10 * math.cos(math.pi / 4)
        vy = 10 * math.sin(math.pi / 4)
        lst = [0, 0, vx, vy]

        def func(w, t):
            return [w[2], w[3], 0, (-9.8 * t) / 6]
        s2 = integrate.odeint(func, lst, t)
        s3 = []
        s4 = []
        for i in range(len(s2)):
            for j in range(0, 4):
                s3.append(s2[i][j])
                s4.append(s[i][j])
        s5 = [s3[i] - s4[i] for i in range(len(s4))]
        max2 = max(s5, key=abs) / max(s4, key=abs)
        assert (abs(max1) < 0.001)
        assert (abs(max2) < 0.001)
