# This file is generated from pydcs_export.lua
from enum import Enum
from typing import Any, Dict, List, Set

from dcs.weapons_data import Weapons
import dcs.task as task
from dcs.unittype import FlyingType
from dcs.liveries_scanner import Liveries

class PlaneType(FlyingType):
    pass


class Tornado_GR4(PlaneType):
    id = "Tornado GR4"
    height = 5.7
    width = 13.91
    length = 16.7
    fuel_max = 4663
    max_speed = 2340
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    livery_name = "TORNADO GR4"  # from type

    class Pylon1:
        BOZ_107___Countermeasure_Dispenser = (1, Weapons.BOZ_107___Countermeasure_Dispenser)
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)

    class Pylon2:
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        ALARM = (3, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        GBU_16___1000lb_Laser_Guided_Bomb = (4, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        ALARM = (4, Weapons.ALARM)
        Sea_Eagle___ASM = (4, Weapons.Sea_Eagle___ASM)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (4, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    class Pylon5:
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (5, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (6, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)

    class Pylon7:
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (7, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)

    class Pylon8:
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (8, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)

    class Pylon9:
        GBU_16___1000lb_Laser_Guided_Bomb = (9, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        ALARM = (9, Weapons.ALARM)
        Sea_Eagle___ASM = (9, Weapons.Sea_Eagle___ASM)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (9, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    class Pylon10:
        ALARM = (10, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon11:
        TORNADO_Fuel_tank = (11, Weapons.TORNADO_Fuel_tank)

    class Pylon12:
        BOZ_107___Countermeasure_Dispenser = (12, Weapons.BOZ_107___Countermeasure_Dispenser)
        Sky_Shadow_ECM_Pod = (12, Weapons.Sky_Shadow_ECM_Pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.PinpointStrike, task.GroundAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.GroundAttack


class Tornado_IDS(PlaneType):
    id = "Tornado IDS"
    height = 5.7
    width = 13.91
    length = 16.7
    fuel_max = 4663
    max_speed = 2340
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    livery_name = "TORNADO IDS"  # from type

    class Pylon1:
        BOZ_107___Countermeasure_Dispenser = (1, Weapons.BOZ_107___Countermeasure_Dispenser)
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)

    class Pylon2:
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Kormoran___ASM = (2, Weapons.Kormoran___ASM)
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        GBU_16___1000lb_Laser_Guided_Bomb = (4, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (4, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Kormoran___ASM = (4, Weapons.Kormoran___ASM)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon8:
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon9:
        GBU_16___1000lb_Laser_Guided_Bomb = (9, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (9, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Kormoran___ASM = (9, Weapons.Kormoran___ASM)

    class Pylon10:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon11:
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (11, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Kormoran___ASM = (11, Weapons.Kormoran___ASM)
        TORNADO_Fuel_tank = (11, Weapons.TORNADO_Fuel_tank)

    class Pylon12:
        BOZ_107___Countermeasure_Dispenser = (12, Weapons.BOZ_107___Countermeasure_Dispenser)
        Sky_Shadow_ECM_Pod = (12, Weapons.Sky_Shadow_ECM_Pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.PinpointStrike, task.GroundAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.GroundAttack


class F_A_18A(PlaneType):
    id = "F/A-18A"
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 6531
    max_speed = 1920
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "F_A-18A"  # from type

    class Pylon1:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        AGM_84A_Harpoon_ASM = (2, Weapons.AGM_84A_Harpoon_ASM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (2, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (2, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (2, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (2, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (2, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon3:
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (3, Weapons.AGM_84A_Harpoon_ASM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_330_gal = (3, Weapons.Fuel_tank_330_gal)

    class Pylon4:
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
#ERRR {6C0D552F-570B-42ff-9F6D-F10D9C1D4E1C}

    class Pylon5:
        Fuel_tank_330_gal = (5, Weapons.Fuel_tank_330_gal)

    class Pylon6:
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_ = (6, Weapons.AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_)

    class Pylon7:
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (7, Weapons.AGM_84A_Harpoon_ASM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (7, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_330_gal = (7, Weapons.Fuel_tank_330_gal)

    class Pylon8:
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        AGM_84A_Harpoon_ASM = (8, Weapons.AGM_84A_Harpoon_ASM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (8, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (8, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (8, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (8, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon9:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class F_A_18C(PlaneType):
    id = "F/A-18C"
    flyable = True
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 4900
    max_speed = 1920
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
        2: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Hornet",
            "Squid",
            "Ragin",
            "Roman",
            "Sting",
            "Jury",
            "Joker",
            "Ram",
            "Hawk",
            "Devil",
            "Check",
            "Snake",
        ]
    }

    livery_name = "F_A-18C"  # from type

    class Pylon1:
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        AGM_84A_Harpoon_ASM = (2, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (2, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_ = (2, Weapons.AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (2, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (2, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (2, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (2, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (2, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        LAU_115_2_LAU_127_AIM_9M = (2, Weapons.LAU_115_2_LAU_127_AIM_9M)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (3, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_330_gal_ = (3, Weapons.Fuel_tank_330_gal_)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (3, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (3, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
#ERRR {6C0D552F-570B-42ff-9F6D-F10D9C1D4E1C}

    class Pylon5:
        Fuel_tank_330_gal_ = (5, Weapons.Fuel_tank_330_gal_)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (6, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (6, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
        AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_ = (6, Weapons.AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_)

    class Pylon7:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (7, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (7, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (7, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_330_gal_ = (7, Weapons.Fuel_tank_330_gal_)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (7, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (7, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        AGM_84A_Harpoon_ASM = (8, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (8, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (8, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_ = (8, Weapons.AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (8, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (8, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_115_2_LAU_127_AIM_9M = (8, Weapons.LAU_115_2_LAU_127_AIM_9M)

    class Pylon9:
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class F_14A(PlaneType):
    id = "F-14A"
    large_parking_slot = True
    height = 4.88
    width = 19.54
    length = 19.1
    fuel_max = 7348
    max_speed = 2490
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "F-14A"  # from type

    class Pylon1:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (2, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)
        AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon3:
        Fuel_tank_367_gal = (3, Weapons.Fuel_tank_367_gal)

    class Pylon4:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (4, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)

    class Pylon5:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (5, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)

    class Pylon6:
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon7:
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon8:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (8, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)

    class Pylon9:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (9, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)

    class Pylon10:
        Fuel_tank_367_gal = (10, Weapons.Fuel_tank_367_gal)

    class Pylon11:
        AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar = (11, Weapons.AIM_54C_Mk47_Phoenix_IN__Semi_Active_Radar)
        AIM_7M_Sparrow_Semi_Active_Radar = (11, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)

    class Pylon12:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (12, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (12, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (12, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (12, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (12, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance]
    task_default = task.Intercept


class Tu_22M3(PlaneType):
    id = "Tu-22M3"
    large_parking_slot = True
    height = 11.05
    width = 34.28
    length = 46.12
    fuel_max = 50000
    max_speed = 2300
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "TU-22M3"  # from type

    class Pylon1:
        Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr = (1, Weapons.Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr)
        MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD = (1, Weapons.MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon2:
        MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD = (2, Weapons.MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon3:
        Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr = (3, Weapons.Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr)
        _33_x_FAB_500_M_62___500kg_GP_Bombs_LD = (3, Weapons._33_x_FAB_500_M_62___500kg_GP_Bombs_LD)
        _33_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons._33_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon4:
        MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon5:
        Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr = (5, Weapons.Kh_22__AS_4_Kitchen____1000kg__AShM__IN__Act_Pas_Rdr)
        MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U9M_with_9_x_FAB_250___250kg_GP_Bombs_LD)

    pylons: Set[int] = {1, 2, 3, 4, 5}

    tasks = [task.AntishipStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.AntishipStrike


class F_4E(PlaneType):
    id = "F-4E"
    height = 5
    width = 11.68
    length = 19.2
    fuel_max = 4864
    max_speed = 2370
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "F-4E"  # from type

    class Pylon1:
        GBU_10___2000lb_Laser_Guided_Bomb = (1, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (1, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        MER6_with_6_x_Mk_82___500lb_GP_Bombs_LD = (1, Weapons.MER6_with_6_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (1, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (1, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        F_4_Fuel_tank_W = (1, Weapons.F_4_Fuel_tank_W)
        LAU_118a_with_AGM_45B_Shrike_ARM__Imp_ = (1, Weapons.LAU_118a_with_AGM_45B_Shrike_ARM__Imp_)
        AGM_45A_Shrike_ARM = (1, Weapons.AGM_45A_Shrike_ARM)

    class Pylon2:
        LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM = (2, Weapons.LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM)
        LAU_7_with_2_x_AIM_9M_Sidewinder_IR_AAM = (2, Weapons.LAU_7_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        LAU_7_with_2_x_AIM_9P_Sidewinder_IR_AAM = (2, Weapons.LAU_7_with_2_x_AIM_9P_Sidewinder_IR_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (2, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        LAU_88_with_2_x_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (2, Weapons.LAU_88_with_2_x_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (2, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_118a_with_AGM_45B_Shrike_ARM__Imp_ = (2, Weapons.LAU_118a_with_AGM_45B_Shrike_ARM__Imp_)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_7_with_AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.LAU_7_with_AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AGM_45A_Shrike_ARM = (2, Weapons.AGM_45A_Shrike_ARM)

    class Pylon3:
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        ALQ_131___ECM_Pod = (3, Weapons.ALQ_131___ECM_Pod)
        AIM_7E_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon4:
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon5:
        F_4_Fuel_tank_C = (5, Weapons.F_4_Fuel_tank_C)

    class Pylon6:
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon7:
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon8:
        LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM = (8, Weapons.LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM)
        LAU_7_with_2_x_AIM_9M_Sidewinder_IR_AAM = (8, Weapons.LAU_7_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        LAU_7_with_2_x_AIM_9P_Sidewinder_IR_AAM = (8, Weapons.LAU_7_with_2_x_AIM_9P_Sidewinder_IR_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (8, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        LAU_88_with_2_x_AGM_65K___Maverick_K__CCD_Imp_ASM__ = (8, Weapons.LAU_88_with_2_x_AGM_65K___Maverick_K__CCD_Imp_ASM__)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (8, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_118a_with_AGM_45B_Shrike_ARM__Imp_ = (8, Weapons.LAU_118a_with_AGM_45B_Shrike_ARM__Imp_)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        AGM_45A_Shrike_ARM = (8, Weapons.AGM_45A_Shrike_ARM)

    class Pylon9:
        GBU_10___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (9, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        MER6_with_6_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.MER6_with_6_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (9, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        F_4_Fuel_tank_W = (9, Weapons.F_4_Fuel_tank_W)
        LAU_118a_with_AGM_45B_Shrike_ARM__Imp_ = (9, Weapons.LAU_118a_with_AGM_45B_Shrike_ARM__Imp_)
        AGM_45A_Shrike_ARM = (9, Weapons.AGM_45A_Shrike_ARM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.GroundAttack, task.CAS, task.PinpointStrike, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class B_52H(PlaneType):
    id = "B-52H"
    large_parking_slot = True
    height = 12.4
    width = 56.4
    length = 49.05
    fuel_max = 141135
    max_speed = 1000
    chaff = 1125
    flare = 192
    charge_total = 1317
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Buff",
            "Dump",
            "Kenworth",
        ]
    }

    livery_name = "B-52H"  # from type

    class Pylon1:
        MER12_with_12_x_Mk_82___500lb_GP_Bombs_LD = (1, Weapons.MER12_with_12_x_Mk_82___500lb_GP_Bombs_LD)
        HSAB_with_9_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (1, Weapons.HSAB_with_9_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        HSAB_with_9_x_Mk_83___1000lb_GP_Bombs_LD = (1, Weapons.HSAB_with_9_x_Mk_83___1000lb_GP_Bombs_LD)
        _6_x_AGM_86D_on_MER = (1, Weapons._6_x_AGM_86D_on_MER)

    class Pylon2:
        _27_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons._27_x_Mk_82___500lb_GP_Bombs_LD)
        _8_x_AGM_86D = (2, Weapons._8_x_AGM_86D)
        _8_x_AGM_86C = (2, Weapons._8_x_AGM_86C)
        _8_x_AGM_84A_Harpoon_ASM = (2, Weapons._8_x_AGM_84A_Harpoon_ASM)

    class Pylon3:
        MER12_with_12_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.MER12_with_12_x_Mk_82___500lb_GP_Bombs_LD)
        HSAB_with_9_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (3, Weapons.HSAB_with_9_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        HSAB_with_9_x_Mk_83___1000lb_GP_Bombs_LD = (3, Weapons.HSAB_with_9_x_Mk_83___1000lb_GP_Bombs_LD)
        _6_x_AGM_86D_on_MER = (3, Weapons._6_x_AGM_86D_on_MER)
#ERRR {HSAB*9 GBU-31}

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.AntishipStrike, task.CAS]
    task_default = task.GroundAttack


class MiG_27K(PlaneType):
    id = "MiG-27K"
    height = 5.64
    width = 14
    length = 16.7
    fuel_max = 4500
    max_speed = 1810
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "MIG-27K"  # from type

    class Pylon2:
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (2, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (2, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (2, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (2, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (2, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (2, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (2, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (2, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (2, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon3:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)

    class Pylon4:
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon5:
        Fuel_tank_800L = (5, Weapons.Fuel_tank_800L)

    class Pylon6:
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon7:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (7, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (7, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (7, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (7, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)

    class Pylon8:
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (8, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (8, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (8, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (8, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (8, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (8, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (8, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (8, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (8, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    pylons: Set[int] = {2, 3, 4, 5, 6, 7, 8}

    tasks = [task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AntishipStrike]
    task_default = task.GroundAttack


class Su_27(PlaneType):
    id = "Su-27"
    flyable = True
    height = 5.932
    width = 14.7
    length = 21.935
    fuel_max = 9400
    max_speed = 2500
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    livery_name = "SU-27"  # from type

    class Pylon1:
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)

    class Pylon3:
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
        _2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator = (3, Weapons._2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator)
        _2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons._2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        _2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons._2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        _2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons._2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        _2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons._2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        _2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP = (3, Weapons._2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP)

    class Pylon4:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (4, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (4, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    class Pylon6:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (6, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (6, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon7:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (7, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (7, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)

    class Pylon8:
        R_73__AA_11_Archer____Infra_Red = (8, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (8, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (8, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (8, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (8, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        Smoke_Generator___red = (8, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (8, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (8, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (8, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (8, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (8, Weapons.Smoke_Generator___orange)
        _2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator = (8, Weapons._2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator)
        _2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons._2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        _2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons._2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        _2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons._2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        _2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons._2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        _2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP = (8, Weapons._2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP)

    class Pylon9:
        R_73__AA_11_Archer____Infra_Red = (9, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (9, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (9, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (9, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (9, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (9, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (9, Weapons.Smoke_Generator___orange)

    class Pylon10:
        R_73__AA_11_Archer____Infra_Red = (10, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__right_ = (10, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Intercept, task.Escort, task.FighterSweep, task.AFAC, task.GroundAttack, task.RunwayAttack, task.AntishipStrike, task.CAS]
    task_default = task.CAP


class MiG_23MLD(PlaneType):
    id = "MiG-23MLD"
    height = 5.772
    width = 14
    length = 15.7
    fuel_max = 3800
    max_speed = 2500
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "MIG-23MLD"  # from type

    class Pylon2:
        R_24R__AA_7_Apex_SA____Semi_Act_Rdr = (2, Weapons.R_24R__AA_7_Apex_SA____Semi_Act_Rdr)
        R_24T__AA_7_Apex_IR____Infra_Red = (2, Weapons.R_24T__AA_7_Apex_IR____Infra_Red)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon3:
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon4:
        Fuel_tank_800L = (4, Weapons.Fuel_tank_800L)

    class Pylon5:
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (5, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (5, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon6:
        R_24R__AA_7_Apex_SA____Semi_Act_Rdr = (6, Weapons.R_24R__AA_7_Apex_SA____Semi_Act_Rdr)
        R_24T__AA_7_Apex_IR____Infra_Red = (6, Weapons.R_24T__AA_7_Apex_IR____Infra_Red)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (6, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    pylons: Set[int] = {2, 3, 4, 5, 6}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.GroundAttack, task.CAS]
    task_default = task.CAP


class Su_25(PlaneType):
    id = "Su-25"
    flyable = True
    height = 4.8
    width = 14.35
    length = 15.36
    fuel_max = 2835
    max_speed = 980
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    livery_name = "SU-25"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (2, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (2, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (2, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (2, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (3, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (3, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (4, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (4, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (4, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (4, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (4, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (4, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (5, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (5, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (5, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (5, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (5, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon6:
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (6, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (6, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (6, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (6, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (6, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (6, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (6, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (6, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (6, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (7, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (7, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (7, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (7, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (7, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (7, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (7, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (7, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (7, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (7, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (7, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (7, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (8, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (8, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (8, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (8, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (8, Weapons.Fuel_tank_800L_Wing)
        SPS_141___ECM_Jamming_Pod = (8, Weapons.SPS_141___ECM_Jamming_Pod)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (9, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (9, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (9, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (9, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (9, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (9, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (9, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (9, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (9, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (9, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (9, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (9, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (9, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (9, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (9, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (9, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (9, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (9, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (9, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (9, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (9, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (9, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (9, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)

    class Pylon10:
        R_60M__AA_8_Aphid____Infra_Red = (10, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_25TM(PlaneType):
    id = "Su-25TM"
    height = 5.2
    width = 14.36
    length = 15.35
    fuel_max = 3790
    max_speed = 950
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "SU-25TM"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        MPS_410 = (1, Weapons.MPS_410)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (2, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (2, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (2, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (2, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        R_73__AA_11_Archer____Infra_Red_ = (2, Weapons.R_73__AA_11_Archer____Infra_Red_)
        R_77__AA_12_Adder____Active_Rdr_ = (2, Weapons.R_77__AA_12_Adder____Active_Rdr_)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (3, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (3, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (3, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (3, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (4, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (4, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        APU_8___8_9A4172_Vikhr = (4, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (4, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (4, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (4, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (4, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (4, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (4, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (5, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500Kr___500kg_TV_Guided_Bomb = (5, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (5, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (5, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (5, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (5, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr_ = (5, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr_)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr_ = (5, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr_)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr_ = (5, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr_)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (5, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (5, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon6:
        Mercury_LLTV_Pod = (6, Weapons.Mercury_LLTV_Pod)
        Kopyo_radar_pod = (6, Weapons.Kopyo_radar_pod)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (7, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (7, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500Kr___500kg_TV_Guided_Bomb = (7, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (7, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (7, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (7, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (7, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr_ = (7, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr_)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr_ = (7, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr_)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr_ = (7, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr_)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (7, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (7, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (7, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (7, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (7, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (7, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (7, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (7, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (7, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (8, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (8, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (8, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        APU_8___8_9A4172_Vikhr = (8, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (8, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (8, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (8, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (8, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (9, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (9, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (9, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (9, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (9, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (9, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (9, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (9, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (9, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (9, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (9, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (9, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (9, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (9, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (9, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (9, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (9, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (9, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (9, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (9, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (9, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (9, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (9, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (9, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (9, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (9, Weapons.Fuel_tank_800L_Wing)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (9, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon10:
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (10, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (10, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (10, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (10, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (10, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (10, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (10, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (10, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (10, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (10, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (10, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (10, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (10, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (10, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (10, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (10, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (10, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (10, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (10, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (10, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (10, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (10, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (10, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        R_73__AA_11_Archer____Infra_Red_ = (10, Weapons.R_73__AA_11_Archer____Infra_Red_)

    class Pylon11:
        R_60M__AA_8_Aphid____Infra_Red = (11, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        MPS_410_ = (11, Weapons.MPS_410_)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.SEAD, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_25T(PlaneType):
    id = "Su-25T"
    flyable = True
    height = 5.2
    width = 14.36
    length = 15.35
    fuel_max = 3790
    max_speed = 950
    chaff = 128
    flare = 128
    charge_total = 256
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    livery_name = "SU-25T"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        MPS_410 = (1, Weapons.MPS_410)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (2, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (2, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (2, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (2, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        R_73__AA_11_Archer____Infra_Red_ = (2, Weapons.R_73__AA_11_Archer____Infra_Red_)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (3, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (3, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (3, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (3, Weapons.Fuel_tank_800L_Wing)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (3, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon4:
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (4, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (4, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        APU_8___8_9A4172_Vikhr = (4, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (4, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (4, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (4, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (4, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (4, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (4, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon5:
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (5, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500Kr___500kg_TV_Guided_Bomb = (5, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (5, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (5, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (5, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (5, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (5, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (5, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (5, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon6:
        Mercury_LLTV_Pod = (6, Weapons.Mercury_LLTV_Pod)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        B_8M1___20_S_8OFP2 = (7, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (7, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (7, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500Kr___500kg_TV_Guided_Bomb = (7, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_ = (7, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser_)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_ = (7, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided_)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (7, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (7, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (7, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (7, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (7, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (7, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (7, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (7, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (7, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (7, Weapons.Fuel_tank_800L_Wing)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (7, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (8, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (8, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (8, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        APU_8___8_9A4172_Vikhr = (8, Weapons.APU_8___8_9A4172_Vikhr)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (8, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (8, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (8, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (8, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon9:
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (9, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (9, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (9, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (9, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (9, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (9, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (9, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (9, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (9, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (9, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (9, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (9, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (9, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (9, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (9, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_ = (9, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr_)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_ = (9, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser_)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (9, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (9, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (9, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (9, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (9, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (9, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (9, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (9, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        Fuel_tank_800L_Wing = (9, Weapons.Fuel_tank_800L_Wing)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (9, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon10:
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (10, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (10, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (10, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        FAB_250___250kg_GP_Bomb_LD = (10, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (10, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (10, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (10, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (10, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (10, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (10, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (10, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (10, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (10, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (10, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (10, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (10, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (10, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (10, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (10, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (10, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (10, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (10, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        S_25L___320Kg__340mm_Laser_Guided_Rkt = (10, Weapons.S_25L___320Kg__340mm_Laser_Guided_Rkt)
        R_73__AA_11_Archer____Infra_Red_ = (10, Weapons.R_73__AA_11_Archer____Infra_Red_)

    class Pylon11:
        R_60M__AA_8_Aphid____Infra_Red = (11, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        MPS_410_ = (11, Weapons.MPS_410_)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.SEAD, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Su_33(PlaneType):
    id = "Su-33"
    flyable = True
    height = 5.72
    width = 14.7
    length = 21.18
    fuel_max = 9500
    max_speed = 2300
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    livery_name = "SU-33"  # from type

    class Pylon1:
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)

    class Pylon3:
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        _2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator = (3, Weapons._2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator)
        _2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons._2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        _2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons._2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        _2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons._2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        _2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons._2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        _2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP = (3, Weapons._2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon4:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (4, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (4, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (4, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (4, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (4, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon5:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon6:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (6, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (6, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon7:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (7, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (7, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon8:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (8, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (8, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Smoke_Generator___red = (8, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (8, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (8, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (8, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (8, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (8, Weapons.Smoke_Generator___orange)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon9:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (9, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (9, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (9, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (9, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (9, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (9, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (9, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (9, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (9, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (9, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (9, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (9, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (9, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (9, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (9, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (9, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (9, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Smoke_Generator___red = (9, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (9, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (9, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (9, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (9, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (9, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (9, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (9, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SAB_100___100kg_flare_illumination_Bomb = (9, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon10:
        R_73__AA_11_Archer____Infra_Red = (10, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (10, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (10, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (10, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (10, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        FAB_250___250kg_GP_Bomb_LD = (10, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (10, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (10, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (10, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (10, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (10, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (10, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (10, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (10, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (10, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (10, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (10, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (10, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (10, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (10, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)
        B_8M1___20_S_8OFP2 = (10, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (10, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SAB_100___100kg_flare_illumination_Bomb = (10, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        _2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator = (10, Weapons._2_x_S_25_OFM___340mm_UnGdrocket__480kg_Penetrator)
        _2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag = (10, Weapons._2_x_S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        _2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (10, Weapons._2_x_B_13L_pods___10_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        _2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (10, Weapons._2_x_B_8M1_pods___40_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        _2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk = (10, Weapons._2_x_B_8V20A_pods___40_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        _2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP = (10, Weapons._2_x_B_8V20A_pods___40_x_S_8OFP2__80mm_UnGd_Rkts__HE_Frag_AP)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (10, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD = (10, Weapons.MBD3_U6_68_with_3_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon11:
        R_73__AA_11_Archer____Infra_Red = (11, Weapons.R_73__AA_11_Archer____Infra_Red)
        FAB_250___250kg_GP_Bomb_LD = (11, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (11, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (11, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Smoke_Generator___red = (11, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (11, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (11, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (11, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (11, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (11, Weapons.Smoke_Generator___orange)

    class Pylon12:
        R_73__AA_11_Archer____Infra_Red = (12, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__right_ = (12, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (12, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (12, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (12, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (12, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (12, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (12, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.CAS, task.GroundAttack, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MiG_25PD(PlaneType):
    id = "MiG-25PD"
    height = 6.1
    width = 14
    length = 23.82
    fuel_max = 15245
    max_speed = 3000
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "MIG-25PD"  # from type

    class Pylon1:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (1, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (1, Weapons.R_40T__AA_6_Acrid____Infra_Red)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon2:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (2, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (2, Weapons.R_40T__AA_6_Acrid____Infra_Red)

    class Pylon3:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (3, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (3, Weapons.R_40T__AA_6_Acrid____Infra_Red)

    class Pylon4:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (4, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (4, Weapons.R_40T__AA_6_Acrid____Infra_Red)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (4, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.Intercept


class MiG_25RBT(PlaneType):
    id = "MiG-25RBT"
    height = 6.1
    width = 14
    length = 23.82
    fuel_max = 15245
    max_speed = 3000

    livery_name = "MIG-25RBT"  # from type

    class Pylon1:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (1, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (1, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (1, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (1, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (1, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (1, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)

    class Pylon2:
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)

    class Pylon3:
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)

    class Pylon4:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (4, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (4, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.Reconnaissance, task.AFAC, task.GroundAttack]
    task_default = task.Reconnaissance


class Su_30(PlaneType):
    id = "Su-30"
    height = 6.36
    width = 14.7
    length = 21.9
    fuel_max = 9400
    max_speed = 2200
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "SU-30"  # from type

    class Pylon1:
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (2, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon3:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (3, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (3, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (3, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (3, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (3, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (3, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (3, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (3, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (3, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (3, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (3, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (3, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (3, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon4:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (4, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (4, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (4, Weapons.R_77__AA_12_Adder____Active_Rdr)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (4, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (4, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (4, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (4, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (4, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (4, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (4, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon5:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (5, Weapons.R_77__AA_12_Adder____Active_Rdr)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (5, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (5, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (5, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (5, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (5, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (5, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (5, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD_ = (5, Weapons.MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD_)

    class Pylon6:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (6, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (6, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (6, Weapons.R_77__AA_12_Adder____Active_Rdr)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (6, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (6, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (6, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (6, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon7:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (7, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (7, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (7, Weapons.R_77__AA_12_Adder____Active_Rdr)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (7, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (7, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (7, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (7, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (7, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (7, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (7, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon8:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (8, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (8, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (8, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (8, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (8, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_73__AA_11_Archer____Infra_Red = (8, Weapons.R_73__AA_11_Archer____Infra_Red)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (8, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (8, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (8, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (8, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (8, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KAB_500LG___500kg_Laser_Guided_Bomb = (8, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (8, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (8, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (8, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (8, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (8, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (8, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon9:
        R_73__AA_11_Archer____Infra_Red = (9, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (9, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon10:
        R_73__AA_11_Archer____Infra_Red = (10, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__right_ = (10, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.SEAD, task.AntishipStrike, task.CAS, task.PinpointStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.CAP


class Su_17M4(PlaneType):
    id = "Su-17M4"
    height = 5.129
    width = 13.68
    length = 19.26
    fuel_max = 3770
    max_speed = 1860
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "SU-17M4"  # from type

    class Pylon1:
        B_8M1___20_S_8OFP2 = (1, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (1, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (1, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (1, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (1, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (1, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (1, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (1, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (1, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (1, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (1, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (1, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (1, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Fuel_tank_1150L = (1, Weapons.Fuel_tank_1150L)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (1, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (1, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (1, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (1, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (1, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (1, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (1, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (1, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (1, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon2:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon3:
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (3, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (3, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (3, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (3, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (3, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr = (3, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        SPS_141___ECM_Jamming_Pod = (3, Weapons.SPS_141___ECM_Jamming_Pod)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (3, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon4:
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (4, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        Fuel_tank_1150L = (4, Weapons.Fuel_tank_1150L)
        Fuel_tank_800L = (4, Weapons.Fuel_tank_800L)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        Kh_28__AS_9_Kyle____720kg__ARM__Pas_Rdr = (4, Weapons.Kh_28__AS_9_Kyle____720kg__ARM__Pas_Rdr)

    class Pylon5:
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (5, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        Fuel_tank_1150L = (5, Weapons.Fuel_tank_1150L)
        Fuel_tank_800L = (5, Weapons.Fuel_tank_800L)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon6:
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (6, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (6, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (6, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (6, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (6, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr = (6, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (6, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (6, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (6, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (6, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod = (6, Weapons.SPPU_22_1___2_x_23mm__GSh_23L_Autocannon_Pod)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (6, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon7:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (7, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon8:
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        FAB_100___100kg_GP_Bomb_LD = (8, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (8, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (8, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U4T_with_4_x_FAB_250___250kg_GP_Bombs_LD)
        MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_2_x_FAB_250___250kg_GP_Bombs_LD)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (8, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (8, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Fuel_tank_1150L = (8, Weapons.Fuel_tank_1150L)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (8, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (8, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.GroundAttack, task.CAS, task.PinpointStrike, task.SEAD, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.GroundAttack


class MiG_31(PlaneType):
    id = "MiG-31"
    height = 6.15
    width = 13.46
    length = 22.7
    fuel_max = 15500
    max_speed = 3000
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "MIG-31"  # from type

    class Pylon1:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (1, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (1, Weapons.R_40T__AA_6_Acrid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon2:
        R_33__AA_9_Amos____Semi_Act_Rdr = (2, Weapons.R_33__AA_9_Amos____Semi_Act_Rdr)

    class Pylon3:
        R_33__AA_9_Amos____Semi_Act_Rdr = (3, Weapons.R_33__AA_9_Amos____Semi_Act_Rdr)

    class Pylon4:
        R_33__AA_9_Amos____Semi_Act_Rdr = (4, Weapons.R_33__AA_9_Amos____Semi_Act_Rdr)

    class Pylon5:
        R_33__AA_9_Amos____Semi_Act_Rdr = (5, Weapons.R_33__AA_9_Amos____Semi_Act_Rdr)

    class Pylon6:
        R_40R__AA_6_Acrid____Semi_Act_Rdr = (6, Weapons.R_40R__AA_6_Acrid____Semi_Act_Rdr)
        R_40T__AA_6_Acrid____Infra_Red = (6, Weapons.R_40T__AA_6_Acrid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (6, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.Intercept


class Tu_95MS(PlaneType):
    id = "Tu-95MS"
    large_parking_slot = True
    height = 13.3
    width = 50.04
    length = 49.13
    fuel_max = 87000
    max_speed = 830
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "TU-95MS"  # from type

    class Pylon1:
        _6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC = (1, Weapons._6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC)

    pylons: Set[int] = {1}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class Su_24M(PlaneType):
    id = "Su-24M"
    height = 4.97
    width = 17.64
    length = 24.53
    fuel_max = 11700
    max_speed = 1700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "SU-24M"  # from type

    class Pylon1:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (1, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (1, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (1, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (1, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (1, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (1, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (1, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (1, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (1, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (1, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (1, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (1, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon2:
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (2, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (2, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (2, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (2, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (2, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr = (2, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (2, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (2, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (2, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (2, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (2, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (2, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (2, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (2, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (2, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (2, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (2, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (2, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (2, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        Fuel_tank_3000L = (2, Weapons.Fuel_tank_3000L)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (2, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon3:
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (3, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (3, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon4:
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (4, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (4, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (4, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (4, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)

    class Pylon5:
        Fuel_tank_2000L = (5, Weapons.Fuel_tank_2000L)
        L_081_Fantasmagoria_ELINT_pod = (5, Weapons.L_081_Fantasmagoria_ELINT_pod)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)

    class Pylon6:
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (6, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (6, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon7:
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser = (7, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided = (7, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr = (7, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr = (7, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr = (7, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (7, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (7, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (7, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (7, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        KAB_500LG___500kg_Laser_Guided_Bomb = (7, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (7, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (7, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (7, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (7, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (7, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (7, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (7, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (7, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (7, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (7, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (7, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (7, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (7, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        Fuel_tank_3000L = (7, Weapons.Fuel_tank_3000L)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (7, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    class Pylon8:
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (8, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (8, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (8, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (8, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (8, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr = (8, Weapons.Kh_25MPU__Updated_AS_12_Kegler____320kg__ARM__IN__Pas_Rdr)
        Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided = (8, Weapons.Kh_25MR__AS_10_Karen____300kg__ASM__10km__RC_Guided)
        Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr = (8, Weapons.Kh_25MP__AS_12_Kegler____320kg__ARM__Pas_Rdr)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.GroundAttack, task.CAS, task.AntishipStrike, task.SEAD, task.PinpointStrike, task.AFAC, task.RunwayAttack]
    task_default = task.GroundAttack


class Su_24MR(PlaneType):
    id = "Su-24MR"
    height = 4.97
    width = 17.64
    length = 24.53
    fuel_max = 11700
    max_speed = 1700
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "SU-24MR"  # from type

    class Pylon1:
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon2:
        Fuel_tank_3000L = (2, Weapons.Fuel_tank_3000L)

    class Pylon5:
        Fuel_tank_2000L = (5, Weapons.Fuel_tank_2000L)
        Tangazh_ELINT_pod = (5, Weapons.Tangazh_ELINT_pod)
        Shpil_2_Laser_Recon__Intel_Pod = (5, Weapons.Shpil_2_Laser_Recon__Intel_Pod)

    class Pylon7:
        Fuel_tank_3000L = (7, Weapons.Fuel_tank_3000L)

    class Pylon8:
        ETHER = (8, Weapons.ETHER)

    pylons: Set[int] = {1, 2, 5, 7, 8}

    tasks = [task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class Tu_160(PlaneType):
    id = "Tu-160"
    large_parking_slot = True
    height = 13.25
    width = 55.7
    length = 54.1
    fuel_max = 157000
    max_speed = 2200
    chaff = 72
    flare = 72
    charge_total = 144
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "TU-160"  # from type

    class Pylon1:
        _6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC = (1, Weapons._6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC)

    class Pylon2:
        _6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC = (2, Weapons._6_x_Kh_65__AS_15B_Kent____1250kg__ASM__IN__MCC)

    pylons: Set[int] = {1, 2}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class F_117A(PlaneType):
    id = "F-117A"
    height = 3.78
    width = 13.2
    length = 20.08
    fuel_max = 8255
    max_speed = 1000

    livery_name = "F-117A"  # from type

    class Pylon1:
        GBU_10___2000lb_Laser_Guided_Bomb = (1, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (1, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    class Pylon2:
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (2, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    pylons: Set[int] = {1, 2}

    tasks = [task.PinpointStrike]
    task_default = task.PinpointStrike


class B_1B(PlaneType):
    id = "B-1B"
    large_parking_slot = True
    height = 10.36
    width = 41.67
    length = 44.81
    fuel_max = 88450
    max_speed = 1530
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Bone",
            "Dark",
            "Vader",
        ]
    }

    livery_name = "B-1B"  # from type

    class Pylon1:
        MK_82_28 = (1, Weapons.MK_82_28)
        CBU87_10 = (1, Weapons.CBU87_10)
        CBU97_10 = (1, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (1, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (1, Weapons.GBU_31_8)
        GBU_31V3B_8 = (1, Weapons.GBU_31V3B_8)
        _4_x_AGM_154C___JSOW_Unitary_BROACH = (1, Weapons._4_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_38_16 = (1, Weapons.GBU_38_16)

    class Pylon2:
        MK_82_28 = (2, Weapons.MK_82_28)
        CBU87_10 = (2, Weapons.CBU87_10)
        CBU97_10 = (2, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (2, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (2, Weapons.GBU_31_8)
        GBU_31V3B_8 = (2, Weapons.GBU_31V3B_8)
        _4_x_AGM_154C___JSOW_Unitary_BROACH = (2, Weapons._4_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_38_16 = (2, Weapons.GBU_38_16)

    class Pylon3:
        MK_82_28 = (3, Weapons.MK_82_28)
        CBU87_10 = (3, Weapons.CBU87_10)
        CBU97_10 = (3, Weapons.CBU97_10)
        B_1B_Mk_84_8 = (3, Weapons.B_1B_Mk_84_8)
        GBU_31_8 = (3, Weapons.GBU_31_8)
        GBU_31V3B_8 = (3, Weapons.GBU_31V3B_8)
        _4_x_AGM_154C___JSOW_Unitary_BROACH = (3, Weapons._4_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_38_16 = (3, Weapons.GBU_38_16)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS]
    task_default = task.GroundAttack


class S_3B(PlaneType):
    id = "S-3B"
    large_parking_slot = True
    height = 6.93
    width = 20.93
    length = 16.26
    fuel_max = 5500
    max_speed = 840
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "S-3B"  # from type

    class Pylon1:
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (1, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (1, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (1, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (1, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (1, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (1, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        AGM_84A_Harpoon_ASM = (1, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (1, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (1, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        Fuel_tank_S_3 = (1, Weapons.Fuel_tank_S_3)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon3:
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (4, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (5, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon6:
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (6, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (6, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (6, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (6, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (6, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        AGM_84A_Harpoon_ASM = (6, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (6, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (6, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        Fuel_tank_S_3 = (6, Weapons.Fuel_tank_S_3)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.GroundAttack, task.AntishipStrike, task.PinpointStrike]
    task_default = task.AntishipStrike


class S_3B_Tanker(PlaneType):
    id = "S-3B Tanker"
    large_parking_slot = True
    height = 6.93
    width = 20.93
    length = 16.26
    fuel_max = 7813
    max_speed = 840
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "S-3B TANKER"  # from type

    pylons: Set[int] = set()

    tasks = [task.Refueling]
    task_default = task.Refueling


class Mirage_2000_5(PlaneType):
    id = "Mirage 2000-5"
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3160
    max_speed = 2340
    chaff = 112
    flare = 16
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "MIRAGE 2000-5"  # from type

    class Pylon1:
        R550_Magic_2_IR_AAM = (1, Weapons.R550_Magic_2_IR_AAM)

    class Pylon2:
        Super_530D = (2, Weapons.Super_530D)
        MICA_RF = (2, Weapons.MICA_RF)
        MICA_IR = (2, Weapons.MICA_IR)
        M2000_Fuel_tank = (2, Weapons.M2000_Fuel_tank)

    class Pylon3:
        MICA_IR = (3, Weapons.MICA_IR)
        MICA_RF = (3, Weapons.MICA_RF)

    class Pylon4:
        MICA_IR = (4, Weapons.MICA_IR)
        MICA_RF = (4, Weapons.MICA_RF)

    class Pylon5:
        M2000_Fuel_tank = (5, Weapons.M2000_Fuel_tank)

    class Pylon6:
        MICA_IR = (6, Weapons.MICA_IR)
        MICA_RF = (6, Weapons.MICA_RF)

    class Pylon7:
        MICA_IR = (7, Weapons.MICA_IR)
        MICA_RF = (7, Weapons.MICA_RF)

    class Pylon8:
        Super_530D = (8, Weapons.Super_530D)
        MICA_RF = (8, Weapons.MICA_RF)
        MICA_IR = (8, Weapons.MICA_IR)
        M2000_Fuel_tank = (8, Weapons.M2000_Fuel_tank)

    class Pylon9:
        R550_Magic_2_IR_AAM = (9, Weapons.R550_Magic_2_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.Reconnaissance]
    task_default = task.CAP


class F_15C(PlaneType):
    id = "F-15C"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2650
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    livery_name = "F-15C"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        Fuel_tank_610_gal = (2, Weapons.Fuel_tank_610_gal)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon5:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon6:
        Fuel_tank_610_gal = (6, Weapons.Fuel_tank_610_gal)

    class Pylon7:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7E_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7E_Sparrow_Semi_Active_Radar)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon10:
        Fuel_tank_610_gal = (10, Weapons.Fuel_tank_610_gal)

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (11, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (11, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class F_15E(PlaneType):
    id = "F-15E"
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 10246
    max_speed = 2650
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Dude",
            "Thud",
            "Gunny",
            "Mad",
            "Trek",
            "Sniper",
            "Sled",
            "Best",
            "Jazz",
            "Rage",
            "Tahoe",
        ]
    }

    livery_name = "F-15E"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        Fuel_tank_610_gal = (2, Weapons.Fuel_tank_610_gal)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (2, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (2, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (2, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (2, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (2, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65H = (2, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (2, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (2, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (4, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (5, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (5, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (5, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (5, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (5, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (5, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (6, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (6, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (6, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (6, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (7, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (7, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)

    class Pylon8:
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (8, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon9:
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (9, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (9, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (9, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (9, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (9, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (9, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (9, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (9, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (9, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)

    class Pylon10:
        Fuel_tank_610_gal = (10, Weapons.Fuel_tank_610_gal)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (10, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (10, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (10, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (10, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (10, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (10, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (10, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (10, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (10, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (10, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)

    class Pylon11:
        Mk_82___500lb_GP_Bomb_LD = (11, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (11, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (11, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (11, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (11, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (11, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (11, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (11, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (11, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (11, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (11, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (11, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (11, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (11, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)

    class Pylon12:
        Mk_82___500lb_GP_Bomb_LD = (12, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (12, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (12, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (12, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (12, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (12, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (12, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (12, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (12, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon13:
        Mk_82___500lb_GP_Bomb_LD = (13, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (13, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (13, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (13, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (13, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (13, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (13, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (13, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (13, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (13, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (13, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (13, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (13, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (13, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)

    class Pylon14:
        Mk_82___500lb_GP_Bomb_LD = (14, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (14, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (14, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (14, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (14, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (14, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (14, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (14, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (14, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon15:
        Mk_82___500lb_GP_Bomb_LD = (15, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (15, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (15, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (15, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (15, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (15, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (15, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (15, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (15, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon16:
        Mk_82___500lb_GP_Bomb_LD = (16, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (16, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_12___500lb_Laser_Guided_Bomb = (16, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (16, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (16, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (16, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (16, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (16, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (16, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)

    class Pylon17:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (17, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (17, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (17, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (17, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (17, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (17, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon18:
        Fuel_tank_610_gal = (18, Weapons.Fuel_tank_610_gal)
        Mk_82___500lb_GP_Bomb_LD = (18, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (18, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (18, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (18, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (18, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (18, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (18, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (18, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (18, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (18, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        CBU_87___202_x_CEM_Cluster_Bomb = (18, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (18, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (18, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (18, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (18, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (18, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65H = (18, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (18, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        AGM_154C___JSOW_Unitary_BROACH = (18, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        LAU_117_AGM_65G = (18, Weapons.LAU_117_AGM_65G)

    class Pylon19:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (19, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (19, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (19, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (19, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (19, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (19, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (19, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance]
    task_default = task.GroundAttack


class MiG_29A(PlaneType):
    id = "MiG-29A"
    flyable = True
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3376
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    livery_name = "MIG-29A"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>

    class Pylon2:
        R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)

    class Pylon3:
        R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon4:
        Fuel_tank_1400L = (4, Weapons.Fuel_tank_1400L)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (5, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (5, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (5, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon6:
        R_60M__AA_8_Aphid____Infra_Red = (6, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (6, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)

    class Pylon7:
        R_60M__AA_8_Aphid____Infra_Red = (7, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (7, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.GroundAttack, task.CAS, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MiG_29G(PlaneType):
    id = "MiG-29G"
    flyable = True
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3376
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    livery_name = "MIG-29G"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>

    class Pylon2:
        R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)

    class Pylon3:
        R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon4:
        Fuel_tank_1400L = (4, Weapons.Fuel_tank_1400L)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (5, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (5, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (5, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon6:
        R_60M__AA_8_Aphid____Infra_Red = (6, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (6, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)

    class Pylon7:
        R_60M__AA_8_Aphid____Infra_Red = (7, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (7, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC]
    task_default = task.CAP


class MiG_29S(PlaneType):
    id = "MiG-29S"
    flyable = True
    height = 4.73
    width = 11.36
    length = 20.32
    fuel_max = 3493
    max_speed = 2450
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    livery_name = "MIG-29S"  # from type

    class Pylon1:
        R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        R_77__AA_12_Adder____Active_Rdr = (1, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon2:
        R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (2, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (2, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_77__AA_12_Adder____Active_Rdr = (2, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon3:
        R_60M__AA_8_Aphid____Infra_Red = (3, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_77__AA_12_Adder____Active_Rdr = (3, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (3, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon4:
        Fuel_tank_1400L = (4, Weapons.Fuel_tank_1400L)
        Smoke_Generator___red = (4, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (4, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (4, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (4, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (4, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (4, Weapons.Smoke_Generator___orange)

    class Pylon5:
        R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (5, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (5, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_77__AA_12_Adder____Active_Rdr = (5, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27T__AA_10_Alamo_B____Infra_Red = (5, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (5, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        Fuel_tank_1150L_MiG_29 = (5, Weapons.Fuel_tank_1150L_MiG_29)

    class Pylon6:
        R_60M__AA_8_Aphid____Infra_Red = (6, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (6, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        B_8M1___20_S_8OFP2 = (6, Weapons.B_8M1___20_S_8OFP2)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        R_77__AA_12_Adder____Active_Rdr = (6, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon7:
        R_60M__AA_8_Aphid____Infra_Red = (7, Weapons.R_60M__AA_8_Aphid____Infra_Red)
        R_73__AA_11_Archer____Infra_Red = (7, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (7, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (7, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (7, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (7, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (7, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (7, Weapons.Smoke_Generator___orange)
#ERRR <CLEAN>
        R_77__AA_12_Adder____Active_Rdr = (7, Weapons.R_77__AA_12_Adder____Active_Rdr)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AFAC, task.GroundAttack, task.CAS, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class Tu_142(PlaneType):
    id = "Tu-142"
    large_parking_slot = True
    height = 13.3
    width = 50.04
    length = 49.13
    fuel_max = 87000
    max_speed = 860
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "TU-142"  # from type

    class Pylon1:
        _6_x_Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (1, Weapons._6_x_Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)

    pylons: Set[int] = {1}

    tasks = [task.AntishipStrike, task.Reconnaissance]
    task_default = task.AntishipStrike


class C_130(PlaneType):
    id = "C-130"
    large_parking_slot = True
    height = 11.66
    width = 40.4
    length = 29.79
    fuel_max = 20830
    max_speed = 610
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    livery_name = "C-130"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class An_26B(PlaneType):
    id = "An-26B"
    large_parking_slot = True
    height = 8.575
    width = 29.2
    length = 23.8
    fuel_max = 5500
    max_speed = 540
    chaff = 384
    flare = 384
    charge_total = 768
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "AN-26B"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class An_30M(PlaneType):
    id = "An-30M"
    large_parking_slot = True
    height = 8.575
    width = 29.2
    length = 23.8
    fuel_max = 8300
    max_speed = 540
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "AN-30M"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport, task.Reconnaissance]
    task_default = task.Transport


class C_17A(PlaneType):
    id = "C-17A"
    large_parking_slot = True
    height = 16.79
    width = 51.76
    length = 53.04
    fuel_max = 132405
    max_speed = 850
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2

    livery_name = "C-17A"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class A_50(PlaneType):
    id = "A-50"
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 70000
    max_speed = 850
    chaff = 192
    flare = 192
    charge_total = 384
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "AWACS"  #{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}

    livery_name = "A-50"  # from type

    pylons: Set[int] = set()

    tasks = [task.AWACS]
    task_default = task.AWACS


class E_3A(PlaneType):
    id = "E-3A"
    large_parking_slot = True
    height = 12.93
    width = 44.4
    length = 46.61
    fuel_max = 65000
    max_speed = 860
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "AWACS"  #{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}

    livery_name = "E-3A"  # from type

    pylons: Set[int] = set()

    tasks = [task.AWACS]
    task_default = task.AWACS


class IL_78M(PlaneType):
    id = "IL-78M"
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 90000
    max_speed = 850
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "IL-78M"  # from type

    pylons: Set[int] = set()

    tasks = [task.Refueling]
    task_default = task.Refueling


class E_2C(PlaneType):
    id = "E-2C"
    large_parking_slot = True
    height = 5.59
    width = 24.56
    length = 17.55
    fuel_max = 5624
    max_speed = 610
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "AWACS"  #{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}

    livery_name = "E-2C"  # from type

    pylons: Set[int] = set()

    tasks = [task.AWACS]
    task_default = task.AWACS


class IL_76MD(PlaneType):
    id = "IL-76MD"
    large_parking_slot = True
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 80000
    max_speed = 850
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "IL-76MD"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class F_16C_bl_50(PlaneType):
    id = "F-16C bl.50"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Viper",
            "Venom",
            "Lobo",
            "Cowboy",
            "Python",
            "Rattler",
            "Panther",
            "Wolf",
            "Weasel",
            "Wild",
            "Ninja",
            "Jedi",
        ]
    }

    livery_name = "F-16C BL.50"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (2, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        _2xGBU_12___500lb_Laser_Guided_Bomb = (3, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (3, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (4, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (4, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (4, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (4, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (7, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (7, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (8, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        _2xGBU_12___500lb_Laser_Guided_Bomb_ = (8, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb_)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (8, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (8, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon10:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16C_bl_52d(PlaneType):
    id = "F-16C bl.52d"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Viper",
            "Venom",
            "Lobo",
            "Cowboy",
            "Python",
            "Rattler",
            "Panther",
            "Wolf",
            "Weasel",
            "Wild",
            "Ninja",
            "Jedi",
        ]
    }

    livery_name = "F-16C BL.52D"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (2, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        _2xGBU_12___500lb_Laser_Guided_Bomb = (3, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (3, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        AGM_154A___JSOW_CEB__CBU_type_ = (3, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154B___JSOW_Anti_Armour = (3, Weapons.AGM_154B___JSOW_Anti_Armour)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (4, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (4, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (4, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (4, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154A___JSOW_CEB__CBU_type_ = (4, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154B___JSOW_Anti_Armour = (4, Weapons.AGM_154B___JSOW_Anti_Armour)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        AGM_154C___JSOW_Unitary_BROACH = (7, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (7, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (7, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154A___JSOW_CEB__CBU_type_ = (7, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154B___JSOW_Anti_Armour = (7, Weapons.AGM_154B___JSOW_Anti_Armour)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (8, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        _2xGBU_12___500lb_Laser_Guided_Bomb_ = (8, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb_)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (8, Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        AGM_154A___JSOW_CEB__CBU_type_ = (8, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154B___JSOW_Anti_Armour = (8, Weapons.AGM_154B___JSOW_Anti_Armour)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (8, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon10:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16A(PlaneType):
    id = "F-16A"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "F-16A"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (2, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (3, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        AGM_119B_Penguin_ASM = (3, Weapons.AGM_119B_Penguin_ASM)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (4, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (4, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (4, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (7, Weapons.BRU_42_with_3_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (8, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (8, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        AGM_119B_Penguin_ASM = (8, Weapons.AGM_119B_Penguin_ASM)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (8, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon10:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class F_16A_MLU(PlaneType):
    id = "F-16A MLU"
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3104
    max_speed = 2150
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    livery_name = "F-16A MLU"  # from type

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon2:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (2, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        AGM_119B_Penguin_ASM = (3, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        _2xGBU_12___500lb_Laser_Guided_Bomb = (3, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (3, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon4:
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        AGM_119B_Penguin_ASM = (4, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (4, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (4, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)

    class Pylon5:
        Lantirn_F_16 = (5, Weapons.Lantirn_F_16)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        Fuel_tank_300_gal = (6, Weapons.Fuel_tank_300_gal)

    class Pylon7:
        Fuel_tank_370_gal = (7, Weapons.Fuel_tank_370_gal)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        AGM_119B_Penguin_ASM = (7, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (7, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        AGM_119B_Penguin_ASM = (8, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_R = (8, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (8, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        _2xGBU_12___500lb_Laser_Guided_Bomb_ = (8, Weapons._2xGBU_12___500lb_Laser_Guided_Bomb_)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (8, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (9, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)

    class Pylon10:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (10, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (10, Weapons.AIM_9L_Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.AFAC, task.Reconnaissance, task.AntishipStrike]
    task_default = task.CAP


class RQ_1A_Predator(PlaneType):
    id = "RQ-1A Predator"
    group_size_max = 1
    height = 2.21
    width = 14.8
    length = 8.13
    fuel_max = 200
    max_speed = 220
    eplrs = True
    radio_frequency = 127.5

    livery_name = "RQ-1A PREDATOR"  # from type

    class Pylon1:
        AGM_114K = (1, Weapons.AGM_114K)

    class Pylon2:
        AGM_114K = (2, Weapons.AGM_114K)

    pylons: Set[int] = {1, 2}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class Yak_40(PlaneType):
    id = "Yak-40"
    large_parking_slot = True
    height = 6.5
    width = 25
    length = 20.36
    fuel_max = 3080
    max_speed = 570

    livery_name = "YAK-40"  # from type

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class KC_135(PlaneType):
    id = "KC-135"
    large_parking_slot = True
    height = 12.93
    width = 40
    length = 46.61
    fuel_max = 90700
    max_speed = 980
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "KC-135"  # from type

    pylons: Set[int] = set()

    tasks = [task.Refueling]
    task_default = task.Refueling


class FW_190D9(PlaneType):
    id = "FW-190D9"
    flyable = True
    height = 4.77
    width = 10.5
    length = 12.13
    fuel_max = 388
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 38.4

    panel_radio = {
        1: {
            "channels": {
                2: 40,
                3: 41,
                1: 39,
                4: 42,
                5: 38
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "FW_MW50TankContents": 1,
    }

    class Properties:

        class FW_MW50TankContents:
            id = "FW_MW50TankContents"

            class Values:
                Empty = 0
                MW_50_Mix = 1
                B_4_Gasoline = 2

    livery_name = "FW-190D9"  # from type

    class Pylon1:
        FW109_FUEL_TANK = (1, Weapons.FW109_FUEL_TANK)
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        ER_4_SC50 = (1, Weapons.ER_4_SC50)

    class Pylon2:
        _13_R4M_3_2kg_UnGd_air_to_air_rocket = (2, Weapons._13_R4M_3_2kg_UnGd_air_to_air_rocket)
        Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket = (2, Weapons.Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket)

    class Pylon3:
        _13_R4M_3_2kg_UnGd_air_to_air_rocket_ = (3, Weapons._13_R4M_3_2kg_UnGd_air_to_air_rocket_)
        Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket = (3, Weapons.Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class FW_190A8(PlaneType):
    id = "FW-190A8"
    flyable = True
    height = 4.77
    width = 10.5
    length = 12.13
    fuel_max = 409
    max_speed = 900
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 38.4

    panel_radio = {
        1: {
            "channels": {
                2: 40,
                3: 41,
                1: 39,
                4: 42,
                5: 38
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "FW_MW50TankContents": 0,
    }

    class Properties:

        class FW_MW50TankContents:
            id = "FW_MW50TankContents"

            class Values:
                Empty = 0
                Additional_fuel = 2

    livery_name = "FW-190A8"  # from type
#ERRR <CLEAN>

    class Pylon1:
        ER_4_SC50 = (1, Weapons.ER_4_SC50)
        SC_501_SC250 = (1, Weapons.SC_501_SC250)
        SC_250_Type_1_L2___250kg_GP_Bomb_LD = (1, Weapons.SC_250_Type_1_L2___250kg_GP_Bomb_LD)
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        SC_500_L2___500kg_GP_Bomb_LD = (1, Weapons.SC_500_L2___500kg_GP_Bomb_LD)
        SD_250_Stg___250kg_GP_Bomb_LD = (1, Weapons.SD_250_Stg___250kg_GP_Bomb_LD)
        SD_500_A___500kg_GP_Bomb_LD = (1, Weapons.SD_500_A___500kg_GP_Bomb_LD)
        AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions = (1, Weapons.AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions)
        AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions = (1, Weapons.AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions)
        AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions = (1, Weapons.AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions)
        BF109K_4_FUEL_TANK = (1, Weapons.BF109K_4_FUEL_TANK)

    class Pylon2:
        Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket = (2, Weapons.Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket)

    class Pylon3:
        Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket = (3, Weapons.Werfer_Granate_21___21_cm_UnGd_air_to_air_rocket)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class Bf_109K_4(PlaneType):
    id = "Bf-109K-4"
    flyable = True
    height = 4.77
    width = 10.5
    length = 12.13
    fuel_max = 296
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 40

    panel_radio = {
        1: {
            "channels": {
                2: 40,
                3: 41,
                1: 39,
                4: 42,
                5: 38
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "MW50TankContents": 1,
        "Flare_Gun": 1,
    }

    class Properties:

        class MW50TankContents:
            id = "MW50TankContents"

            class Values:
                Empty = 0
                MW_50_Mix = 1
                B_4_Gasoline = 2

        class Flare_Gun:
            id = "Flare_Gun"

            class Values:
                None_ = 0
                Flare_Gun = 1

    livery_name = "BF-109K-4"  # from type

    class Pylon1:
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        SC_501_SC250 = (1, Weapons.SC_501_SC250)
        BF109K_4_FUEL_TANK = (1, Weapons.BF109K_4_FUEL_TANK)

    pylons: Set[int] = {1}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class SpitfireLFMkIX(PlaneType):
    id = "SpitfireLFMkIX"
    flyable = True
    height = 4.77
    width = 11.25
    length = 12.13
    fuel_max = 247
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                2: 124,
                3: 131,
                1: 105,
                4: 139,
                5: 108.9
            },
        },
    }

    livery_name = "SPITFIRELFMKIX"  # from type

    class Pylon1:
        British_GP_250LBS_Bomb_MK4_on_LH_Spitfire_Wing_Carrier = (1, Weapons.British_GP_250LBS_Bomb_MK4_on_LH_Spitfire_Wing_Carrier)
        Beer_Bomb__L__on_LH_Spitfire_Wing_Carrier = (1, Weapons.Beer_Bomb__L__on_LH_Spitfire_Wing_Carrier)
        Beer_Bomb__D__on_LH_Spitfire_Wing_Carrier = (1, Weapons.Beer_Bomb__D__on_LH_Spitfire_Wing_Carrier)

    class Pylon2:
        SPITFIRE_45GAL_SLIPPER_TANK = (2, Weapons.SPITFIRE_45GAL_SLIPPER_TANK)
        SPITFIRE_45GAL_TORPEDO_TANK = (2, Weapons.SPITFIRE_45GAL_TORPEDO_TANK)
        British_GP_500LBS_Bomb_MK4_on_British_UniversalBC_MK3 = (2, Weapons.British_GP_500LBS_Bomb_MK4_on_British_UniversalBC_MK3)

    class Pylon3:
        British_GP_250LBS_Bomb_MK4_on_RH_Spitfire_Wing_Carrier = (3, Weapons.British_GP_250LBS_Bomb_MK4_on_RH_Spitfire_Wing_Carrier)
        Beer_Bomb__L__on_RH_Spitfire_Wing_Carrier = (3, Weapons.Beer_Bomb__L__on_RH_Spitfire_Wing_Carrier)
        Beer_Bomb__D__on_RH_Spitfire_Wing_Carrier = (3, Weapons.Beer_Bomb__D__on_RH_Spitfire_Wing_Carrier)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class SpitfireLFMkIXCW(PlaneType):
    id = "SpitfireLFMkIXCW"
    flyable = True
    height = 4.77
    width = 11.25
    length = 12.13
    fuel_max = 247
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                2: 124,
                3: 131,
                1: 105,
                4: 139,
                5: 108.9
            },
        },
    }

    livery_name = "SPITFIRELFMKIXCW"  # from type

    class Pylon1:
        British_GP_250LBS_Bomb_MK4_on_LH_Spitfire_Wing_Carrier = (1, Weapons.British_GP_250LBS_Bomb_MK4_on_LH_Spitfire_Wing_Carrier)
        Beer_Bomb__L__on_LH_Spitfire_Wing_Carrier = (1, Weapons.Beer_Bomb__L__on_LH_Spitfire_Wing_Carrier)
        Beer_Bomb__D__on_LH_Spitfire_Wing_Carrier = (1, Weapons.Beer_Bomb__D__on_LH_Spitfire_Wing_Carrier)

    class Pylon2:
        SPITFIRE_45GAL_SLIPPER_TANK = (2, Weapons.SPITFIRE_45GAL_SLIPPER_TANK)
        SPITFIRE_45GAL_TORPEDO_TANK = (2, Weapons.SPITFIRE_45GAL_TORPEDO_TANK)
        British_GP_500LBS_Bomb_MK4_on_British_UniversalBC_MK3 = (2, Weapons.British_GP_500LBS_Bomb_MK4_on_British_UniversalBC_MK3)

    class Pylon3:
        British_GP_250LBS_Bomb_MK4_on_RH_Spitfire_Wing_Carrier = (3, Weapons.British_GP_250LBS_Bomb_MK4_on_RH_Spitfire_Wing_Carrier)
        Beer_Bomb__L__on_RH_Spitfire_Wing_Carrier = (3, Weapons.Beer_Bomb__L__on_RH_Spitfire_Wing_Carrier)
        Beer_Bomb__D__on_RH_Spitfire_Wing_Carrier = (3, Weapons.Beer_Bomb__D__on_RH_Spitfire_Wing_Carrier)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class P_51D(PlaneType):
    id = "P-51D"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 732
    max_speed = 763.2
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    livery_name = "P-51D"  # from livery_entry

    class Pylon1:
        HVAR__UnGd_Rkt = (1, Weapons.HVAR__UnGd_Rkt)
        HVAR_Smoke_Generator = (1, Weapons.HVAR_Smoke_Generator)

    class Pylon2:
        HVAR__UnGd_Rkt = (2, Weapons.HVAR__UnGd_Rkt)

    class Pylon3:
        HVAR__UnGd_Rkt = (3, Weapons.HVAR__UnGd_Rkt)

    class Pylon4:
        AN_M64___500lb_GP_Bomb_LD = (4, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _75_US_gal__Fuel_Tank = (4, Weapons._75_US_gal__Fuel_Tank)
        HVAR__UnGd_Rkt = (4, Weapons.HVAR__UnGd_Rkt)

    class Pylon5:
        HVAR__UnGd_Rkt = (5, Weapons.HVAR__UnGd_Rkt)

    class Pylon6:
        HVAR__UnGd_Rkt = (6, Weapons.HVAR__UnGd_Rkt)

    class Pylon7:
        AN_M64___500lb_GP_Bomb_LD = (7, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _75_US_gal__Fuel_Tank = (7, Weapons._75_US_gal__Fuel_Tank)
        HVAR__UnGd_Rkt = (7, Weapons.HVAR__UnGd_Rkt)

    class Pylon8:
        HVAR__UnGd_Rkt = (8, Weapons.HVAR__UnGd_Rkt)

    class Pylon9:
        HVAR__UnGd_Rkt = (9, Weapons.HVAR__UnGd_Rkt)

    class Pylon10:
        HVAR__UnGd_Rkt = (10, Weapons.HVAR__UnGd_Rkt)
        HVAR_Smoke_Generator = (10, Weapons.HVAR_Smoke_Generator)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class P_51D_30_NA(PlaneType):
    id = "P-51D-30-NA"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 732
    max_speed = 763.2
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    livery_name = "P-51D"  # from livery_entry

    class Pylon1:
        HVAR__UnGd_Rkt = (1, Weapons.HVAR__UnGd_Rkt)
        HVAR_Smoke_Generator = (1, Weapons.HVAR_Smoke_Generator)

    class Pylon2:
        HVAR__UnGd_Rkt = (2, Weapons.HVAR__UnGd_Rkt)

    class Pylon3:
        HVAR__UnGd_Rkt = (3, Weapons.HVAR__UnGd_Rkt)

    class Pylon4:
        AN_M64___500lb_GP_Bomb_LD = (4, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _75_US_gal__Fuel_Tank = (4, Weapons._75_US_gal__Fuel_Tank)
        HVAR__UnGd_Rkt = (4, Weapons.HVAR__UnGd_Rkt)

    class Pylon5:
        HVAR__UnGd_Rkt = (5, Weapons.HVAR__UnGd_Rkt)

    class Pylon6:
        HVAR__UnGd_Rkt = (6, Weapons.HVAR__UnGd_Rkt)

    class Pylon7:
        AN_M64___500lb_GP_Bomb_LD = (7, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _75_US_gal__Fuel_Tank = (7, Weapons._75_US_gal__Fuel_Tank)
        HVAR__UnGd_Rkt = (7, Weapons.HVAR__UnGd_Rkt)

    class Pylon8:
        HVAR__UnGd_Rkt = (8, Weapons.HVAR__UnGd_Rkt)

    class Pylon9:
        HVAR__UnGd_Rkt = (9, Weapons.HVAR__UnGd_Rkt)

    class Pylon10:
        HVAR__UnGd_Rkt = (10, Weapons.HVAR__UnGd_Rkt)
        HVAR_Smoke_Generator = (10, Weapons.HVAR_Smoke_Generator)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class P_47D_30(PlaneType):
    id = "P-47D-30"
    flyable = True
    height = 4.77
    width = 12.42
    length = 11
    fuel_max = 1007
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "WaterTankContents": 1,
    }

    class Properties:

        class WaterTankContents:
            id = "WaterTankContents"

            class Values:
                Empty = 0
                Water = 1

    livery_name = "P-47D-30"  # from livery_entry

    class Pylon1:
        AN_M30A1___100lb_GP_Bomb_LD = (1, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (1, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (1, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (1, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (1, Weapons._110_US_gal__Fuel_Tank)
#ERRR <CLEAN>

    class Pylon2:
        AN_M30A1___100lb_GP_Bomb_LD = (2, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (2, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (2, Weapons.AN_M64___500lb_GP_Bomb_LD)
        AN_M65___1000lb_GP_Bomb_LD = (2, Weapons.AN_M65___1000lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (2, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (2, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (2, Weapons._150_US_gal__Fuel_Tank)
        M10_Smoke_Tank___red = (2, Weapons.M10_Smoke_Tank___red)
        M10_Smoke_Tank___yellow = (2, Weapons.M10_Smoke_Tank___yellow)
        M10_Smoke_Tank___orange = (2, Weapons.M10_Smoke_Tank___orange)
        M10_Smoke_Tank___green = (2, Weapons.M10_Smoke_Tank___green)
        M10_Smoke_Tank___blue = (2, Weapons.M10_Smoke_Tank___blue)
        M10_Smoke_Tank___white = (2, Weapons.M10_Smoke_Tank___white)
#ERRR <CLEAN>

    class Pylon3:
        AN_M30A1___100lb_GP_Bomb_LD = (3, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (3, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (3, Weapons.AN_M64___500lb_GP_Bomb_LD)
        AN_M65___1000lb_GP_Bomb_LD = (3, Weapons.AN_M65___1000lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (3, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (3, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (3, Weapons._150_US_gal__Fuel_Tank)
        M10_Smoke_Tank___red = (3, Weapons.M10_Smoke_Tank___red)
        M10_Smoke_Tank___yellow = (3, Weapons.M10_Smoke_Tank___yellow)
        M10_Smoke_Tank___orange = (3, Weapons.M10_Smoke_Tank___orange)
        M10_Smoke_Tank___green = (3, Weapons.M10_Smoke_Tank___green)
        M10_Smoke_Tank___blue = (3, Weapons.M10_Smoke_Tank___blue)
        M10_Smoke_Tank___white = (3, Weapons.M10_Smoke_Tank___white)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class P_47D_30bl1(PlaneType):
    id = "P-47D-30bl1"
    flyable = True
    height = 4.77
    width = 12.42
    length = 11
    fuel_max = 1007
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "WaterTankContents": 1,
    }

    class Properties:

        class WaterTankContents:
            id = "WaterTankContents"

            class Values:
                Empty = 0
                Water = 1

    livery_name = "P-47D-30"  # from livery_entry

    class Pylon1:
        AN_M30A1___100lb_GP_Bomb_LD = (1, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (1, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (1, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (1, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (1, Weapons._110_US_gal__Fuel_Tank)
#ERRR <CLEAN>

    class Pylon2:
        AN_M30A1___100lb_GP_Bomb_LD = (2, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (2, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (2, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (2, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (2, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (2, Weapons._150_US_gal__Fuel_Tank)
#ERRR <CLEAN>

    class Pylon3:
        AN_M30A1___100lb_GP_Bomb_LD = (3, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (3, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (3, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (3, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (3, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (3, Weapons._150_US_gal__Fuel_Tank)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class P_47D_40(PlaneType):
    id = "P-47D-40"
    flyable = True
    height = 4.77
    width = 12.42
    length = 11
    fuel_max = 1007
    max_speed = 828
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "WaterTankContents": 1,
    }

    class Properties:

        class WaterTankContents:
            id = "WaterTankContents"

            class Values:
                Empty = 0
                Water = 1

    livery_name = "P-47D-30"  # from livery_entry

    class Pylon1:
        AN_M30A1___100lb_GP_Bomb_LD = (1, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (1, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (1, Weapons.AN_M64___500lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (1, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (1, Weapons._110_US_gal__Fuel_Tank)
#ERRR <CLEAN>

    class Pylon2:
        AN_M30A1___100lb_GP_Bomb_LD = (2, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (2, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (2, Weapons.AN_M64___500lb_GP_Bomb_LD)
        AN_M65___1000lb_GP_Bomb_LD = (2, Weapons.AN_M65___1000lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (2, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (2, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (2, Weapons._150_US_gal__Fuel_Tank)
        M10_Smoke_Tank___red = (2, Weapons.M10_Smoke_Tank___red)
        M10_Smoke_Tank___yellow = (2, Weapons.M10_Smoke_Tank___yellow)
        M10_Smoke_Tank___orange = (2, Weapons.M10_Smoke_Tank___orange)
        M10_Smoke_Tank___green = (2, Weapons.M10_Smoke_Tank___green)
        M10_Smoke_Tank___blue = (2, Weapons.M10_Smoke_Tank___blue)
        M10_Smoke_Tank___white = (2, Weapons.M10_Smoke_Tank___white)
#ERRR <CLEAN>

    class Pylon3:
        AN_M30A1___100lb_GP_Bomb_LD = (3, Weapons.AN_M30A1___100lb_GP_Bomb_LD)
        AN_M57___250lb_GP_Bomb_LD = (3, Weapons.AN_M57___250lb_GP_Bomb_LD)
        AN_M64___500lb_GP_Bomb_LD = (3, Weapons.AN_M64___500lb_GP_Bomb_LD)
        AN_M65___1000lb_GP_Bomb_LD = (3, Weapons.AN_M65___1000lb_GP_Bomb_LD)
        _108_US_gal__Paper_Fuel_Tank = (3, Weapons._108_US_gal__Paper_Fuel_Tank)
        _110_US_gal__Fuel_Tank = (3, Weapons._110_US_gal__Fuel_Tank)
        _150_US_gal__Fuel_Tank = (3, Weapons._150_US_gal__Fuel_Tank)
        M10_Smoke_Tank___red = (3, Weapons.M10_Smoke_Tank___red)
        M10_Smoke_Tank___yellow = (3, Weapons.M10_Smoke_Tank___yellow)
        M10_Smoke_Tank___orange = (3, Weapons.M10_Smoke_Tank___orange)
        M10_Smoke_Tank___green = (3, Weapons.M10_Smoke_Tank___green)
        M10_Smoke_Tank___blue = (3, Weapons.M10_Smoke_Tank___blue)
        M10_Smoke_Tank___white = (3, Weapons.M10_Smoke_Tank___white)

    class Pylon4:
        _5_x_HVAR__UnGd_Rkt = (4, Weapons._5_x_HVAR__UnGd_Rkt)
        _3_x_4_5_inch_M8_UnGd_Rocket = (4, Weapons._3_x_4_5_inch_M8_UnGd_Rocket)

    class Pylon5:
        _5_x_HVAR__UnGd_Rkt_ = (5, Weapons._5_x_HVAR__UnGd_Rkt_)
        _3_x_4_5_inch_M8_UnGd_Rocket = (5, Weapons._3_x_4_5_inch_M8_UnGd_Rocket)

    pylons: Set[int] = {1, 2, 3, 4, 5}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class MosquitoFBMkVI(PlaneType):
    id = "MosquitoFBMkVI"
    flyable = True
    height = 3.81
    width = 16.3
    length = 12.34
    fuel_max = 1483.1
    max_speed = 648
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                2: 124,
                3: 131,
                1: 105,
                4: 139,
                5: 108.9
            },
        },
        2: {
            "channels": {
                6: 5.85,
                2: 8,
                8: 5.65,
                3: 7.71,
                1: 9.255,
                4: 6.872,
                5: 5.955,
                7: 5.75
            },
        },
        4: {
            "channels": {
                6: 0.26,
                2: 0.421,
                8: 0.24,
                3: 0.303,
                1: 0.444,
                4: 0.3,
                5: 0.27,
                7: 0.25
            },
        },
        3: {
            "channels": {
                6: 3.25,
                2: 5,
                8: 3.011,
                3: 4.75,
                1: 5.25,
                4: 4.5,
                5: 4.25,
                7: 3.012
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "Flare_Gun": 1,
        "ResinLights": 0.15,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class Flare_Gun:
            id = "Flare_Gun"

            class Values:
                None_ = 0
                Flare_Gun = 1

        class ResinLights:
            id = "ResinLights"

            class Values:
                Red = 0.15
                Orange = 0.25
                Yellow = 0.35
                Green = 0.45
                Sky = 0.55
                Blue = 0.65
                Violet = 0.75
                White = 0.05

    livery_name = "MOSQUITOFBMKVI"  # from type

    class Pylon1:
        _250_lb_GP_Mk_IV = (1, Weapons._250_lb_GP_Mk_IV)
        _250_lb_GP_Mk_V = (1, Weapons._250_lb_GP_Mk_V)
        _500_lb_GP_Mk_IV = (1, Weapons._500_lb_GP_Mk_IV)
        _500_lb_GP_Short_tail = (1, Weapons._500_lb_GP_Short_tail)
        _500_lb_GP_Mk_V = (1, Weapons._500_lb_GP_Mk_V)
        _250_lb_MC_Mk_I = (1, Weapons._250_lb_MC_Mk_I)
        _250_lb_MC_Mk_II = (1, Weapons._250_lb_MC_Mk_II)
        _500_lb_MC_Short_tail = (1, Weapons._500_lb_MC_Short_tail)
        _500_lb_MC_Mk_II = (1, Weapons._500_lb_MC_Mk_II)
        _500_lb_S_A_P_ = (1, Weapons._500_lb_S_A_P_)
        _50_gal__Drop_Tank = (1, Weapons._50_gal__Drop_Tank)
        _100_gal__Drop_Tank = (1, Weapons._100_gal__Drop_Tank)

    class Pylon2:
        _250_lb_GP_Mk_IV = (2, Weapons._250_lb_GP_Mk_IV)
        _250_lb_GP_Mk_V = (2, Weapons._250_lb_GP_Mk_V)
        _500_lb_GP_Mk_IV = (2, Weapons._500_lb_GP_Mk_IV)
        _500_lb_GP_Short_tail = (2, Weapons._500_lb_GP_Short_tail)
        _500_lb_GP_Mk_V = (2, Weapons._500_lb_GP_Mk_V)
        _250_lb_MC_Mk_I = (2, Weapons._250_lb_MC_Mk_I)
        _250_lb_MC_Mk_II = (2, Weapons._250_lb_MC_Mk_II)
        _500_lb_MC_Short_tail = (2, Weapons._500_lb_MC_Short_tail)
        _500_lb_MC_Mk_II = (2, Weapons._500_lb_MC_Mk_II)
        _500_lb_S_A_P_ = (2, Weapons._500_lb_S_A_P_)
        _50_gal__Drop_Tank = (2, Weapons._50_gal__Drop_Tank)
        _100_gal__Drop_Tank = (2, Weapons._100_gal__Drop_Tank)

    class Pylon3:
        _250_lb_GP_Mk_IV_ = (3, Weapons._250_lb_GP_Mk_IV_)
        _250_lb_GP_Mk_V_ = (3, Weapons._250_lb_GP_Mk_V_)
        _500_lb_GP_Short_tail_ = (3, Weapons._500_lb_GP_Short_tail_)
        _250_lb_MC_Mk_I_ = (3, Weapons._250_lb_MC_Mk_I_)
        _250_lb_MC_Mk_II_ = (3, Weapons._250_lb_MC_Mk_II_)
        _500_lb_MC_Short_tail_ = (3, Weapons._500_lb_MC_Short_tail_)
        _250_lb_S_A_P__ = (3, Weapons._250_lb_S_A_P__)

    class Pylon4:
        _250_lb_GP_Mk_IV_ = (4, Weapons._250_lb_GP_Mk_IV_)
        _250_lb_GP_Mk_V_ = (4, Weapons._250_lb_GP_Mk_V_)
        _500_lb_GP_Short_tail_ = (4, Weapons._500_lb_GP_Short_tail_)
        _250_lb_MC_Mk_I_ = (4, Weapons._250_lb_MC_Mk_I_)
        _250_lb_MC_Mk_II_ = (4, Weapons._250_lb_MC_Mk_II_)
        _500_lb_MC_Short_tail_ = (4, Weapons._500_lb_MC_Short_tail_)
        _250_lb_S_A_P__ = (4, Weapons._250_lb_S_A_P__)

    class Pylon5:
        _4_x_RP_3_60lb_F_No1_Mk_I = (5, Weapons._4_x_RP_3_60lb_F_No1_Mk_I)
        _2_x_RP_3_60lb_F_No1_Mk_I = (5, Weapons._2_x_RP_3_60lb_F_No1_Mk_I)
        _4_x_RP_3_60lb_SAP_No2_Mk_I = (5, Weapons._4_x_RP_3_60lb_SAP_No2_Mk_I)
        _2_x_RP_3_60lb_SAP_No2_Mk_I = (5, Weapons._2_x_RP_3_60lb_SAP_No2_Mk_I)
        _4_x_RP_3_25lb_AP_Mk_I = (5, Weapons._4_x_RP_3_25lb_AP_Mk_I)
        _2_x_RP_3_25lb_AP_Mk_I = (5, Weapons._2_x_RP_3_25lb_AP_Mk_I)

    class Pylon6:
        _4_x_RP_3_60lb_F_No1_Mk_I_ = (6, Weapons._4_x_RP_3_60lb_F_No1_Mk_I_)
        _2_x_RP_3_60lb_F_No1_Mk_I_ = (6, Weapons._2_x_RP_3_60lb_F_No1_Mk_I_)
        _4_x_RP_3_60lb_SAP_No2_Mk_I_ = (6, Weapons._4_x_RP_3_60lb_SAP_No2_Mk_I_)
        _2_x_RP_3_60lb_SAP_No2_Mk_I_ = (6, Weapons._2_x_RP_3_60lb_SAP_No2_Mk_I_)
        _4_x_RP_3_25lb_AP_Mk_I_ = (6, Weapons._4_x_RP_3_25lb_AP_Mk_I_)
        _2_x_RP_3_25lb_AP_Mk_I_ = (6, Weapons._2_x_RP_3_25lb_AP_Mk_I_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAP, task.Escort, task.Intercept, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class A_20G(PlaneType):
    id = "A-20G"
    height = 4.83
    width = 18.69
    length = 14.63
    fuel_max = 1500
    max_speed = 619.2

    callnames: Dict[str, List[str]] = {
        "USA": [
        ]
    }

    property_defaults: Dict[str, Any] = {
    }

    livery_name = "A-20G"  # from type

    class Pylon1:
        _4_x_AN_M64___500lb_GP_Bomb_LD = (1, Weapons._4_x_AN_M64___500lb_GP_Bomb_LD)

    pylons: Set[int] = {1}

    tasks = [task.GroundAttack, task.RunwayAttack, task.CAS, task.AntishipStrike]
    task_default = task.CAS


class A_10A(PlaneType):
    id = "A-10A"
    flyable = True
    height = 4.47
    width = 17.53
    length = 16.26
    fuel_max = 5029
    max_speed = 720
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2
    radio_frequency = 124

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Hawg",
            "Boar",
            "Pig",
            "Tusk",
        ]
    }

    property_defaults: Dict[str, Any] = {
    }

    livery_name = "A-10A"  # from type

    class Pylon1:
        LAU_105_2_AIM_9L = (1, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_L = (1, Weapons.LAU_105_1_AIM_9L_L)
        LAU_105_2_AIM_9P5 = (1, Weapons.LAU_105_2_AIM_9P5)
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (1, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        LAU_105_1_AIM_9M_L = (1, Weapons.LAU_105_1_AIM_9M_L)
        LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM = (1, Weapons.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM)
        ALQ_131___ECM_Pod = (1, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (1, Weapons.ALQ_184)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (1, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (1, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (1, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (1, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        CBU_97___10_x_SFW_Cluster_Bomb = (1, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_105_AIS_ASQ_T50_L = (1, Weapons.LAU_105_AIS_ASQ_T50_L)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (1, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (2, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon3:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        Fuel_Tank_FT600 = (4, Weapons.Fuel_Tank_FT600)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (4, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (5, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (5, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (5, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (5, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        Fuel_Tank_FT600 = (6, Weapons.Fuel_Tank_FT600)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (6, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (7, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon8:
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (8, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (8, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (8, Weapons.BRU_42_3_BDU_33)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        Fuel_Tank_FT600 = (8, Weapons.Fuel_Tank_FT600)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon9:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (9, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (9, Weapons.LAU_117_AGM_65H)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (9, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_88_AGM_65H_2_R = (9, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H_3 = (9, Weapons.LAU_88_AGM_65H_3)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (9, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (9, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (9, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        BRU_42_3_BDU_33 = (9, Weapons.BRU_42_3_BDU_33)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (9, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        CBU_97___10_x_SFW_Cluster_Bomb = (9, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (9, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon10:
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (10, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (10, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (10, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (10, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (10, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    class Pylon11:
        LAU_105_2_AIM_9L = (11, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_R = (11, Weapons.LAU_105_1_AIM_9L_R)
        LAU_105_2_AIM_9P5 = (11, Weapons.LAU_105_2_AIM_9P5)
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (11, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        LAU_105_1_AIM_9M_R = (11, Weapons.LAU_105_1_AIM_9M_R)
        LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM = (11, Weapons.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM)
        ALQ_131___ECM_Pod = (11, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (11, Weapons.ALQ_184)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (11, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (11, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (11, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (11, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        CBU_97___10_x_SFW_Cluster_Bomb = (11, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (11, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_105_AIS_ASQ_T50_R = (11, Weapons.LAU_105_AIS_ASQ_T50_R)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (11, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class A_10C(PlaneType):
    id = "A-10C"
    flyable = True
    height = 4.47
    width = 17.53
    length = 16.26
    fuel_max = 5029
    max_speed = 720
    chaff = 240
    flare = 120
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Hawg",
            "Boar",
            "Pig",
            "Tusk",
        ]
    }

    property_defaults: Dict[str, Any] = {
    }

    livery_name = "A-10C"  # from type

    class Pylon1:
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (1, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_105_1_AIM_9M_L = (1, Weapons.LAU_105_1_AIM_9M_L)
        LAU_105 = (1, Weapons.LAU_105)
        LAU_105_2_CATM_9M = (1, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_L = (1, Weapons.LAU_105_1_CATM_9M_L)
        ALQ_131___ECM_Pod = (1, Weapons.ALQ_131___ECM_Pod)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (1, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (1, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (1, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (1, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (1, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        ALQ_184 = (1, Weapons.ALQ_184)
        CBU_97___10_x_SFW_Cluster_Bomb = (1, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_105_AIS_ASQ_T50_L = (1, Weapons.LAU_105_AIS_ASQ_T50_L)
        LAU_105_2_AIM_9L = (1, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_L = (1, Weapons.LAU_105_1_AIM_9L_L)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        AN_AAQ_28_LITENING___Targeting_Pod = (2, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (2, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)

    class Pylon3:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (3, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (3, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (3, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (3, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (3, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (3, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (3, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (3, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (3, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        BRU_42_LS = (3, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (3, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (3, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (3, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (3, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (3, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (3, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (3, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (3, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Fuel_Tank_FT600 = (4, Weapons.Fuel_Tank_FT600)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (4, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (4, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (4, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (4, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (4, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (4, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (4, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (4, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (4, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (4, Weapons.MXU_648_TP)
        BRU_42_LS = (4, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (4, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (5, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (5, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (5, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (5, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (5, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (5, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        BRU_42_LS = (5, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (5, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (5, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (5, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (5, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (5, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (6, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (6, Weapons.MXU_648_TP)
        BRU_42_LS = (6, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        Fuel_Tank_FT600 = (6, Weapons.Fuel_Tank_FT600)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (7, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (7, Weapons.MXU_648_TP)
        BRU_42_LS = (7, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)

    class Pylon8:
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Fuel_Tank_FT600 = (8, Weapons.Fuel_Tank_FT600)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (8, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (8, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (8, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (8, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (8, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (8, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (8, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (8, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (8, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (8, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (8, Weapons.MXU_648_TP)
        BRU_42_LS = (8, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (8, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (8, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (8, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)

    class Pylon9:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (9, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (9, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (9, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (9, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (9, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (9, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (9, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (9, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (9, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (9, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (9, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (9, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (9, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (9, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (9, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (9, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (9, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (9, Weapons.MXU_648_TP)
        BRU_42_LS = (9, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (9, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (9, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (9, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_R = (9, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (9, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (9, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (9, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (9, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (9, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (9, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (9, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (9, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (9, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (9, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (9, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (9, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (9, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)

    class Pylon10:
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (10, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        AN_AAQ_28_LITENING___Targeting_Pod = (10, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (10, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (10, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (10, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (10, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (10, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)

    class Pylon11:
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (11, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        ALQ_131___ECM_Pod = (11, Weapons.ALQ_131___ECM_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (11, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (11, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (11, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (11, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (11, Weapons.Mk_82___500lb_GP_Bomb_LD)
        CBU_87___202_x_CEM_Cluster_Bomb = (11, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (11, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (11, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_105_1_AIM_9M_R = (11, Weapons.LAU_105_1_AIM_9M_R)
        LAU_105 = (11, Weapons.LAU_105)
        ALQ_184 = (11, Weapons.ALQ_184)
        LAU_105_2_CATM_9M = (11, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_R = (11, Weapons.LAU_105_1_CATM_9M_R)
        LAU_105_AIS_ASQ_T50_R = (11, Weapons.LAU_105_AIS_ASQ_T50_R)
        LAU_105_2_AIM_9L = (11, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_R = (11, Weapons.LAU_105_1_AIM_9L_R)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class A_10C_2(PlaneType):
    id = "A-10C_2"
    flyable = True
    height = 4.47
    width = 17.53
    length = 16.26
    fuel_max = 5029
    max_speed = 720
    chaff = 240
    flare = 240
    charge_total = 480
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Hawg",
            "Boar",
            "Pig",
            "Tusk",
        ]
    }

    property_defaults: Dict[str, Any] = {
    }

    livery_name = "A-10CII"  # from livery_entry

    class Pylon1:
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (1, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_105_1_AIM_9M_L = (1, Weapons.LAU_105_1_AIM_9M_L)
        LAU_105 = (1, Weapons.LAU_105)
        LAU_105_2_CATM_9M = (1, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_L = (1, Weapons.LAU_105_1_CATM_9M_L)
        ALQ_131___ECM_Pod = (1, Weapons.ALQ_131___ECM_Pod)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (1, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (1, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (1, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (1, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (1, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        ALQ_184 = (1, Weapons.ALQ_184)
        CBU_97___10_x_SFW_Cluster_Bomb = (1, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_105_AIS_ASQ_T50_L = (1, Weapons.LAU_105_AIS_ASQ_T50_L)
        LAU_105_2_AIM_9L = (1, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_L = (1, Weapons.LAU_105_1_AIM_9L_L)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        AN_AAQ_28_LITENING___Targeting_Pod = (2, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (2, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)

    class Pylon3:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (3, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65L = (3, Weapons.LAU_117_AGM_65L)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (3, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (3, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (3, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (3, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (3, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (3, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (3, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (3, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        BRU_42_LS = (3, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (3, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (3, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (3, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (3, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (3, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (3, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (3, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (3, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (3, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (3, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (3, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (3, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Fuel_Tank_FT600 = (4, Weapons.Fuel_Tank_FT600)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (4, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (4, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (4, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (4, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (4, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (4, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (4, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (4, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (4, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (4, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (4, Weapons.MXU_648_TP)
        BRU_42_LS = (4, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (4, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (4, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (4, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (4, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (4, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (4, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (5, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (5, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (5, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (5, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (5, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (5, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        BRU_42_LS = (5, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (5, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (5, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (5, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (5, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (5, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (5, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (5, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (6, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (6, Weapons.MXU_648_TP)
        BRU_42_LS = (6, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        Fuel_Tank_FT600 = (6, Weapons.Fuel_Tank_FT600)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (7, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        MXU_648_TP = (7, Weapons.MXU_648_TP)
        BRU_42_LS = (7, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (7, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (7, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (7, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon8:
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Fuel_Tank_FT600 = (8, Weapons.Fuel_Tank_FT600)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (8, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (8, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (8, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (8, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (8, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (8, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (8, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (8, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (8, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (8, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (8, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (8, Weapons.MXU_648_TP)
        BRU_42_LS = (8, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (8, Weapons.BRU_42_3_BDU_33)
        BRU_42_3_GBU_12 = (8, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (8, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (8, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (8, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (8, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (8, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (8, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon9:
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (9, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (9, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (9, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65L = (9, Weapons.LAU_117_AGM_65L)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (9, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (9, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        GBU_10___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (9, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (9, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (9, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (9, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (9, Weapons.BRU_42_with_3_x_LAU_68_pods___21_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
#ERRR {B2DC636E-5E45-42db-81D9-38F3E059107C}
        LAU_131x3_HYDRA_70_MK1 = (9, Weapons.LAU_131x3_HYDRA_70_MK1)
        LAU_131x3_HYDRA_70_MK5 = (9, Weapons.LAU_131x3_HYDRA_70_MK5)
        LAU_131x3_HYDRA_70_MK61 = (9, Weapons.LAU_131x3_HYDRA_70_MK61)
        LAU_131x3_HYDRA_70_M151 = (9, Weapons.LAU_131x3_HYDRA_70_M151)
        LAU_131x3_HYDRA_70_M156 = (9, Weapons.LAU_131x3_HYDRA_70_M156)
        LAU_131x3_HYDRA_70_WTU1B = (9, Weapons.LAU_131x3_HYDRA_70_WTU1B)
        LAU_131x3_HYDRA_70_M257 = (9, Weapons.LAU_131x3_HYDRA_70_M257)
        LAU_131x3_HYDRA_70_M274 = (9, Weapons.LAU_131x3_HYDRA_70_M274)
#ERRR LAU_131x3_HYDRA_70_M278
        MXU_648_TP = (9, Weapons.MXU_648_TP)
        BRU_42_LS = (9, Weapons.BRU_42_LS)
        BRU_42_3_BDU_33 = (9, Weapons.BRU_42_3_BDU_33)
        LAU_117_AGM_65H = (9, Weapons.LAU_117_AGM_65H)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        LAU_88_AGM_65H = (9, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_2_R = (9, Weapons.LAU_88_AGM_65H_2_R)
        LAU_88_AGM_65H_3 = (9, Weapons.LAU_88_AGM_65H_3)
        LAU_117_TGM_65D = (9, Weapons.LAU_117_TGM_65D)
        LAU_117_TGM_65G = (9, Weapons.LAU_117_TGM_65G)
        LAU_117_TGM_65H = (9, Weapons.LAU_117_TGM_65H)
        LAU_117_CATM_65K = (9, Weapons.LAU_117_CATM_65K)
        BRU_42_3_GBU_12 = (9, Weapons.BRU_42_3_GBU_12)
        CBU_97___10_x_SFW_Cluster_Bomb = (9, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (9, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (9, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (9, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (9, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (9, Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (9, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (9, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (9, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (9, Weapons.BRU_42_with_3_x_LAU_131_pods___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (9, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)

    class Pylon10:
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (10, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        AN_AAQ_28_LITENING___Targeting_Pod = (10, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (10, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (10, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (10, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (10, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {1FE353C6-5EB6-4d22-9CFD-6DB384EC7296}
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (10, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (10, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)

    class Pylon11:
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (11, Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (11, Weapons.Smokewinder___orange)
        ALQ_131___ECM_Pod = (11, Weapons.ALQ_131___ECM_Pod)
        GBU_12___500lb_Laser_Guided_Bomb = (11, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (11, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (11, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (11, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (11, Weapons.Mk_82___500lb_GP_Bomb_LD)
        CBU_87___202_x_CEM_Cluster_Bomb = (11, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (11, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (11, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_105_1_AIM_9M_R = (11, Weapons.LAU_105_1_AIM_9M_R)
        LAU_105 = (11, Weapons.LAU_105)
        ALQ_184 = (11, Weapons.ALQ_184)
        LAU_105_2_CATM_9M = (11, Weapons.LAU_105_2_CATM_9M)
        LAU_105_1_CATM_9M_R = (11, Weapons.LAU_105_1_CATM_9M_R)
        LAU_105_AIS_ASQ_T50_R = (11, Weapons.LAU_105_AIS_ASQ_T50_R)
        LAU_105_2_AIM_9L = (11, Weapons.LAU_105_2_AIM_9L)
        LAU_105_1_AIM_9L_R = (11, Weapons.LAU_105_1_AIM_9L_R)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAS


class AJS37(PlaneType):
    id = "AJS37"
    flyable = True
    height = 5.81
    width = 10.6
    length = 16.3
    fuel_max = 4476
    max_speed = 2203.2
    chaff = 210
    flare = 72
    charge_total = 280
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                27: 270,
                2: 264,
                38: 251,
                3: 265,
                4: 256,
                5: 254,
                6: 250,
                7: 270,
                8: 257,
                10: 262,
                12: 268,
                14: 260,
                16: 261,
                20: 266,
                24: 256,
                28: 257,
                32: 268,
                40: 266,
                33: 269,
                41: 305,
                17: 267,
                21: 305,
                25: 254,
                29: 255,
                34: 260,
                42: 264,
                9: 255,
                11: 259,
                13: 269,
                15: 263,
                18: 251,
                22: 264,
                26: 250,
                30: 262,
                36: 261,
                44: 125,
                47: 121.5,
                46: 141,
                39: 253,
                43: 265,
                37: 267,
                45: 121,
                35: 263,
                1: 305,
                19: 253,
                23: 265,
                31: 259
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "Rb04GroupTarget": 3,
        "Rb04VinkelHopp": 0,
        "WeapSafeHeight": 1,
        "MissionGeneratorSetting": 0,
    }

    class Properties:

        class Rb04GroupTarget:
            id = "Rb04GroupTarget"

            class Values:
                First_and_third = 0
                First_and_second = 1
                Second_and_third = 2
                Random = 3

        class Rb04VinkelHopp:
            id = "Rb04VinkelHopp"

            class Values:
                None_ = 0
                Left = 1
                Right = 2
                Both = 3

        class WeapSafeHeight:
            id = "WeapSafeHeight"

            class Values:
                Low = 0
                Medium = 1
                High = 2

        class MissionGeneratorSetting:
            id = "MissionGeneratorSetting"

            class Values:
                Allow_all = 0
                Allow_non_generated = 2
                Disallow_cartridge_switching = 3

    livery_name = "AJS37"  # from type

    class Pylon1:
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (1, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (1, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)

    class Pylon2:
        Rb_74__AIM_9L__Sidewinder_IR_AAM = (2, Weapons.Rb_74__AIM_9L__Sidewinder_IR_AAM)
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (2, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (2, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)
        BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_ = (2, Weapons.BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_ = (2, Weapons.BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_ = (2, Weapons.BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_)
        AKAN_M_55_Gunpod__150_rnds_MINGR55_HE = (2, Weapons.AKAN_M_55_Gunpod__150_rnds_MINGR55_HE)
        ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG = (2, Weapons.ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG)
        ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT = (2, Weapons.ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT)
        Rb_04E_Anti_ship_Missile = (2, Weapons.Rb_04E_Anti_ship_Missile)
        Rb_15F_Programmable_Anti_ship_Missile = (2, Weapons.Rb_15F_Programmable_Anti_ship_Missile)
        RB_04E__for_A_I___with_launcher = (2, Weapons.RB_04E__for_A_I___with_launcher)
        RB_15F__for_A_I___with_launcher = (2, Weapons.RB_15F__for_A_I___with_launcher)
        KB_Flare_Chaff_dispenser_pod = (2, Weapons.KB_Flare_Chaff_dispenser_pod)
        _2x_80kg_LYSB_71_Illumination_Bomb = (2, Weapons._2x_80kg_LYSB_71_Illumination_Bomb)
        _4x_SB_M_71_120kg_GP_Bomb_Low_drag = (2, Weapons._4x_SB_M_71_120kg_GP_Bomb_Low_drag)
        _4x_SB_M_71_120kg_GP_Bomb_High_drag = (2, Weapons._4x_SB_M_71_120kg_GP_Bomb_High_drag)
#ERRR {MERPYLON}
        Rb_75A__AGM_65A_Maverick___TV_ASM_ = (2, Weapons.Rb_75A__AGM_65A_Maverick___TV_ASM_)
        Rb_75B__AGM_65B_Maverick___TV_ASM_ = (2, Weapons.Rb_75B__AGM_65B_Maverick___TV_ASM_)
        Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_ = (2, Weapons.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_)

    class Pylon3:
        Rb_74__AIM_9L__Sidewinder_IR_AAM = (3, Weapons.Rb_74__AIM_9L__Sidewinder_IR_AAM)
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (3, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (3, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)
        BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_ = (3, Weapons.BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_ = (3, Weapons.BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_ = (3, Weapons.BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_)
        ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG = (3, Weapons.ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG)
        ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT = (3, Weapons.ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT)
        Rb_05A_MCLOS_ASM_AShM_AAM = (3, Weapons.Rb_05A_MCLOS_ASM_AShM_AAM)
        _2x_80kg_LYSB_71_Illumination_Bomb = (3, Weapons._2x_80kg_LYSB_71_Illumination_Bomb)
        _4x_SB_M_71_120kg_GP_Bomb_Low_drag = (3, Weapons._4x_SB_M_71_120kg_GP_Bomb_Low_drag)
        _4x_SB_M_71_120kg_GP_Bomb_High_drag = (3, Weapons._4x_SB_M_71_120kg_GP_Bomb_High_drag)
#ERRR {MERPYLON}
        Rb_75A__AGM_65A_Maverick___TV_ASM_ = (3, Weapons.Rb_75A__AGM_65A_Maverick___TV_ASM_)
        Rb_75B__AGM_65B_Maverick___TV_ASM_ = (3, Weapons.Rb_75B__AGM_65B_Maverick___TV_ASM_)
        Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_ = (3, Weapons.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_)

    class Pylon4:
        AJS_External_tank_1013kg_fuel = (4, Weapons.AJS_External_tank_1013kg_fuel)

    class Pylon5:
        Rb_74__AIM_9L__Sidewinder_IR_AAM = (5, Weapons.Rb_74__AIM_9L__Sidewinder_IR_AAM)
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (5, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (5, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)
        BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_ = (5, Weapons.BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_ = (5, Weapons.BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_ = (5, Weapons.BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_)
        ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG = (5, Weapons.ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG)
        ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT = (5, Weapons.ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT)
        Rb_05A_MCLOS_ASM_AShM_AAM = (5, Weapons.Rb_05A_MCLOS_ASM_AShM_AAM)
        _2x_80kg_LYSB_71_Illumination_Bomb = (5, Weapons._2x_80kg_LYSB_71_Illumination_Bomb)
        _4x_SB_M_71_120kg_GP_Bomb_Low_drag = (5, Weapons._4x_SB_M_71_120kg_GP_Bomb_Low_drag)
        _4x_SB_M_71_120kg_GP_Bomb_High_drag = (5, Weapons._4x_SB_M_71_120kg_GP_Bomb_High_drag)
        Rb_75A__AGM_65A_Maverick___TV_ASM_ = (5, Weapons.Rb_75A__AGM_65A_Maverick___TV_ASM_)
        Rb_75B__AGM_65B_Maverick___TV_ASM_ = (5, Weapons.Rb_75B__AGM_65B_Maverick___TV_ASM_)
        Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_ = (5, Weapons.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_)
#ERRR {MERPYLON}

    class Pylon6:
        Rb_74__AIM_9L__Sidewinder_IR_AAM = (6, Weapons.Rb_74__AIM_9L__Sidewinder_IR_AAM)
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (6, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (6, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)
        BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_ = (6, Weapons.BK_90_MJ12__12x_MJ2_HEAT___36x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_ = (6, Weapons.BK_90_MJ1__72_x_MJ1_HE_FRAG_Bomblets_)
        BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_ = (6, Weapons.BK_90_MJ2__24_x_MJ2_HEAT_Bomblets_)
        AKAN_M_55_Gunpod__150_rnds_MINGR55_HE = (6, Weapons.AKAN_M_55_Gunpod__150_rnds_MINGR55_HE)
        ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG = (6, Weapons.ARAK_M_70B_HE_6x_135mm_UnGd_Rkts__Shu70_HE_FRAG)
        ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT = (6, Weapons.ARAK_M_70B_AP_6x_135mm_UnGd_Rkts__Pshu70_HEAT)
        Rb_04E_Anti_ship_Missile = (6, Weapons.Rb_04E_Anti_ship_Missile)
        Rb_15F_Programmable_Anti_ship_Missile = (6, Weapons.Rb_15F_Programmable_Anti_ship_Missile)
        RB_04E__for_A_I___with_launcher = (6, Weapons.RB_04E__for_A_I___with_launcher)
        RB_15F__for_A_I___with_launcher = (6, Weapons.RB_15F__for_A_I___with_launcher)
        KB_Flare_Chaff_dispenser_pod = (6, Weapons.KB_Flare_Chaff_dispenser_pod)
        U_22_Jammer_pod = (6, Weapons.U_22_Jammer_pod)
        U22_A_Jammer = (6, Weapons.U22_A_Jammer)
        _2x_80kg_LYSB_71_Illumination_Bomb = (6, Weapons._2x_80kg_LYSB_71_Illumination_Bomb)
        _4x_SB_M_71_120kg_GP_Bomb_Low_drag = (6, Weapons._4x_SB_M_71_120kg_GP_Bomb_Low_drag)
        _4x_SB_M_71_120kg_GP_Bomb_High_drag = (6, Weapons._4x_SB_M_71_120kg_GP_Bomb_High_drag)
#ERRR {MERPYLON}
        Rb_75A__AGM_65A_Maverick___TV_ASM_ = (6, Weapons.Rb_75A__AGM_65A_Maverick___TV_ASM_)
        Rb_75B__AGM_65B_Maverick___TV_ASM_ = (6, Weapons.Rb_75B__AGM_65B_Maverick___TV_ASM_)
        Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_ = (6, Weapons.Rb_75T__AGM_65A_Maverick___TV_ASM_Lg_HE_Whd_)

    class Pylon7:
        Rb_24J__AIM_9P__Sidewinder_IR_AAM = (7, Weapons.Rb_24J__AIM_9P__Sidewinder_IR_AAM)
        Rb_24__AIM_9B__Sidewinder_IR_AAM = (7, Weapons.Rb_24__AIM_9B__Sidewinder_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.CAP, task.Escort, task.SEAD, task.FighterSweep, task.Intercept, task.AntishipStrike, task.Reconnaissance]
    task_default = task.GroundAttack


class AV8BNA(PlaneType):
    id = "AV8BNA"
    flyable = True
    height = 3.55
    width = 9.24
    length = 14.12
    fuel_max = 3519.423
    max_speed = 990
    chaff = 60
    flare = 120
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 1
    tacan = True
    category = "Air"  #{C168A850-3C0B-436a-95B5-C4A015552560}
    radio_frequency = 243

    panel_radio = {
        1: {
            "channels": {
                1: 177,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                21: 133,
                11: 259,
                22: 257.8,
                3: 265,
                6: 250,
                12: 268,
                24: 123.3,
                25: 344,
                13: 269,
                26: 385,
                7: 270,
                14: 260,
                23: 122.1,
                19: 253,
                15: 263
            },
        },
        2: {
            "channels": {
                1: 133,
                2: 257.8,
                4: 123.3,
                8: 385.4,
                16: 121,
                17: 126,
                9: 139,
                18: 125,
                5: 344,
                10: 140,
                20: 122,
                21: 123,
                11: 134,
                22: 124,
                3: 122.1,
                6: 385,
                12: 132,
                24: 136,
                25: 141,
                13: 131,
                26: 127,
                7: 130,
                14: 129,
                23: 135,
                19: 128,
                15: 138
            },
        },
        3: {
            "channels": {
                1: 177,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                30: 123.3,
                21: 133,
                11: 259,
                22: 257.8,
                3: 265,
                6: 250,
                12: 268,
                24: 123.3,
                19: 253,
                25: 344,
                13: 269,
                26: 385,
                27: 133,
                7: 270,
                14: 260,
                28: 257.8,
                23: 122.1,
                29: 122.1,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "MountNVG": False,
        "ClockTime": 1,
        "RocketBurst": 1,
        "EWDispenserTFL": 1,
        "EWDispenserTFR": 1,
        "EWDispenserTBL": 2,
        "EWDispenserTBR": 2,
        "EWDispenserBL": 2,
        "EWDispenserBR": 2,
        "LaserCode100": 6,
        "LaserCode10": 8,
        "LaserCode1": 8,
        "AAR_Zone1": 0,
        "AAR_Zone2": 0,
        "AAR_Zone3": 0,
    }

    class Properties:

        class MountNVG:
            id = "MountNVG"

        class ClockTime:
            id = "ClockTime"

            class Values:
                ZULU_Time = 1
                Local_Time = 2

        class RocketBurst:
            id = "RocketBurst"

            class Values:
                Single_Fire = 1
                Ripple_Fire = 2

        class EWDispenserTFL:
            id = "EWDispenserTFL"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class EWDispenserTFR:
            id = "EWDispenserTFR"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class EWDispenserTBL:
            id = "EWDispenserTBL"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class EWDispenserTBR:
            id = "EWDispenserTBR"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class EWDispenserBL:
            id = "EWDispenserBL"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class EWDispenserBR:
            id = "EWDispenserBR"

            class Values:
                _30_Chaff = 1
                _30_Flares = 2

        class LaserCode100:
            id = "LaserCode100"

        class LaserCode10:
            id = "LaserCode10"

        class LaserCode1:
            id = "LaserCode1"

        class AAR_Zone1:
            id = "AAR_Zone1"

        class AAR_Zone2:
            id = "AAR_Zone2"

        class AAR_Zone3:
            id = "AAR_Zone3"

    livery_name = "AV8BNA"  # from type

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AGM_122_Sidearm = (1, Weapons.AGM_122_Sidearm)
        Mk_81___250lb_GP_Bomb_LD = (1, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (1, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (1, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (1, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (1, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (1, Weapons.CATM_9M)
        BDU_33___25lb_Practice_Bomb_LD = (1, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)

    class Pylon2:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (2, Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM)
        AGM_122_Sidearm_ = (2, Weapons.AGM_122_Sidearm_)
        Mk_81___250lb_GP_Bomb_LD = (2, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (2, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (2, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (2, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (2, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)
        _2_Mk_82 = (2, Weapons._2_Mk_82)
        _2_Mk_20_Rockeye = (2, Weapons._2_Mk_20_Rockeye)
        _2_CBU_99 = (2, Weapons._2_CBU_99)
        _2_GBU_12 = (2, Weapons._2_GBU_12)
        _2_Mk_82_AIR = (2, Weapons._2_Mk_82_AIR)
        _2_Mk_82_Snakeye = (2, Weapons._2_Mk_82_Snakeye)
        _2_GBU_38 = (2, Weapons._2_GBU_38)
        _2_GBU_54_V_1_B = (2, Weapons._2_GBU_54_V_1_B)
        _3_Mk_81 = (2, Weapons._3_Mk_81)
        _3_Mk_82 = (2, Weapons._3_Mk_82)
        _3_Mk_82_AIR = (2, Weapons._3_Mk_82_AIR)
        _3_Mk_82_Snakeye = (2, Weapons._3_Mk_82_Snakeye)
        _3_GBU_12 = (2, Weapons._3_GBU_12)
        _3_GBU_38 = (2, Weapons._3_GBU_38)
        _3_GBU_54_V_1_B = (2, Weapons._3_GBU_54_V_1_B)
        BDU_33___25lb_Practice_Bomb_LD = (2, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BRU_42_3_BDU_33 = (2, Weapons.BRU_42_3_BDU_33)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65L = (2, Weapons.LAU_117_AGM_65L)
        LAU_117_AGM_65F = (2, Weapons.LAU_117_AGM_65F)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)
        AN_AAQ_28_LITENING___Targeting_Pod = (2, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        Smokewinder___red = (2, Weapons.Smokewinder___red)
        Smokewinder___green = (2, Weapons.Smokewinder___green)
        Smokewinder___blue = (2, Weapons.Smokewinder___blue)
        Smokewinder___white = (2, Weapons.Smokewinder___white)
        Smokewinder___yellow = (2, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (2, Weapons.Smokewinder___orange)
        AERO_1D_300_Gallons_Fuel_Tank_ = (2, Weapons.AERO_1D_300_Gallons_Fuel_Tank_)
        AERO_1D_300_Gallons_Fuel_Tank__Empty_ = (2, Weapons.AERO_1D_300_Gallons_Fuel_Tank__Empty_)

    class Pylon3:
        Mk_81___250lb_GP_Bomb_LD = (3, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (3, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (3, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (3, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (3, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)
        _3_Mk_81 = (3, Weapons._3_Mk_81)
        _2_Mk_82 = (3, Weapons._2_Mk_82)
        _2_Mk_83 = (3, Weapons._2_Mk_83)
        _2_Mk_20_Rockeye = (3, Weapons._2_Mk_20_Rockeye)
        _2_CBU_99 = (3, Weapons._2_CBU_99)
        _2_GBU_12 = (3, Weapons._2_GBU_12)
        _2_Mk_82_AIR = (3, Weapons._2_Mk_82_AIR)
        _2_Mk_82_Snakeye = (3, Weapons._2_Mk_82_Snakeye)
        _2_GBU_38 = (3, Weapons._2_GBU_38)
        _2_GBU_54_V_1_B = (3, Weapons._2_GBU_54_V_1_B)
        BDU_33___25lb_Practice_Bomb_LD = (3, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BRU_42_3_BDU_33 = (3, Weapons.BRU_42_3_BDU_33)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (3, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65L = (3, Weapons.LAU_117_AGM_65L)
        LAU_117_AGM_65F = (3, Weapons.LAU_117_AGM_65F)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (3, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        AN_AAQ_28_LITENING___Targeting_Pod = (3, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        AERO_1D_300_Gallons_Fuel_Tank_ = (3, Weapons.AERO_1D_300_Gallons_Fuel_Tank_)
        AERO_1D_300_Gallons_Fuel_Tank__Empty_ = (3, Weapons.AERO_1D_300_Gallons_Fuel_Tank__Empty_)

    class Pylon4:
        GAU_12_Gunpod_w_SAPHEI_T = (4, Weapons.GAU_12_Gunpod_w_SAPHEI_T)
        GAU_12_Gunpod_w_AP_M79 = (4, Weapons.GAU_12_Gunpod_w_AP_M79)
        GAU_12_Gunpod_w_HE_M792 = (4, Weapons.GAU_12_Gunpod_w_HE_M792)

    class Pylon5:
        AN_ALQ_164_DECM_Pod = (5, Weapons.AN_ALQ_164_DECM_Pod)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    class Pylon6:
        Mk_81___250lb_GP_Bomb_LD = (6, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (6, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (6, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (6, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (6, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (6, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (6, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)
        _3_Mk_81 = (6, Weapons._3_Mk_81)
        _2_Mk_82_ = (6, Weapons._2_Mk_82_)
        _2_Mk_83_ = (6, Weapons._2_Mk_83_)
        _2_Mk_20_Rockeye_ = (6, Weapons._2_Mk_20_Rockeye_)
        _2_CBU_99_ = (6, Weapons._2_CBU_99_)
        _2_GBU_12_ = (6, Weapons._2_GBU_12_)
        _2_Mk_82_AIR_ = (6, Weapons._2_Mk_82_AIR_)
        _2_Mk_82_Snakeye_ = (6, Weapons._2_Mk_82_Snakeye_)
        _2_GBU_38_ = (6, Weapons._2_GBU_38_)
        _2_GBU_54_V_1_B_ = (6, Weapons._2_GBU_54_V_1_B_)
        BDU_33___25lb_Practice_Bomb_LD = (6, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BRU_42_3_BDU_33 = (6, Weapons.BRU_42_3_BDU_33)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (6, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65L = (6, Weapons.LAU_117_AGM_65L)
        LAU_117_AGM_65F = (6, Weapons.LAU_117_AGM_65F)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (6, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (6, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (6, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        AN_AAQ_28_LITENING___Targeting_Pod = (6, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        AERO_1D_300_Gallons_Fuel_Tank_ = (6, Weapons.AERO_1D_300_Gallons_Fuel_Tank_)
        AERO_1D_300_Gallons_Fuel_Tank__Empty_ = (6, Weapons.AERO_1D_300_Gallons_Fuel_Tank__Empty_)

    class Pylon7:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (7, Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM)
        AGM_122_Sidearm_ = (7, Weapons.AGM_122_Sidearm_)
        Mk_81___250lb_GP_Bomb_LD = (7, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (7, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (7, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (7, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (7, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD = (7, Weapons.GBU_54B___LJDAM__500lb_Laser__GPS_Guided_Bomb_LD)
        _2_Mk_82_ = (7, Weapons._2_Mk_82_)
        _2_Mk_20_Rockeye_ = (7, Weapons._2_Mk_20_Rockeye_)
        _2_CBU_99_ = (7, Weapons._2_CBU_99_)
        _2_GBU_12_ = (7, Weapons._2_GBU_12_)
        _2_Mk_82_AIR_ = (7, Weapons._2_Mk_82_AIR_)
        _2_Mk_82_Snakeye_ = (7, Weapons._2_Mk_82_Snakeye_)
        _2_GBU_38_ = (7, Weapons._2_GBU_38_)
        _2_GBU_54_V_1_B_ = (7, Weapons._2_GBU_54_V_1_B_)
        _3_Mk_81 = (7, Weapons._3_Mk_81)
        _3_Mk_82 = (7, Weapons._3_Mk_82)
        _3_Mk_82_AIR = (7, Weapons._3_Mk_82_AIR)
        _3_Mk_82_Snakeye = (7, Weapons._3_Mk_82_Snakeye)
        _3_GBU_12 = (7, Weapons._3_GBU_12)
        _3_GBU_38 = (7, Weapons._3_GBU_38)
        _3_GBU_54_V_1_B = (7, Weapons._3_GBU_54_V_1_B)
        BDU_33___25lb_Practice_Bomb_LD = (7, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BRU_42_3_BDU_33 = (7, Weapons.BRU_42_3_BDU_33)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (7, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65L = (7, Weapons.LAU_117_AGM_65L)
        LAU_117_AGM_65F = (7, Weapons.LAU_117_AGM_65F)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (7, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (7, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
#ERRR {9115A5AF-6D5C-4b6b-BEA9-31D48B5C6001}
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS = (7, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M151__HE_APKWS)
        LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS = (7, Weapons.LAU_131_pod___7_x_2_75_Hydra__Laser_Guided_Rkts_M282__MPP_APKWS)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (7, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares = (7, Weapons.BRU_42_with_3_x_SUU_25_x_8_LUU_2___Target_Marker_Flares)
        AN_AAQ_28_LITENING___Targeting_Pod = (7, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        AERO_1D_300_Gallons_Fuel_Tank_ = (7, Weapons.AERO_1D_300_Gallons_Fuel_Tank_)
        AERO_1D_300_Gallons_Fuel_Tank__Empty_ = (7, Weapons.AERO_1D_300_Gallons_Fuel_Tank__Empty_)

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AGM_122_Sidearm = (8, Weapons.AGM_122_Sidearm)
        Mk_81___250lb_GP_Bomb_LD = (8, Weapons.Mk_81___250lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (8, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (8, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (8, Weapons.CATM_9M)
        BDU_33___25lb_Practice_Bomb_LD = (8, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        Smokewinder___red = (8, Weapons.Smokewinder___red)
        Smokewinder___green = (8, Weapons.Smokewinder___green)
        Smokewinder___blue = (8, Weapons.Smokewinder___blue)
        Smokewinder___white = (8, Weapons.Smokewinder___white)
        Smokewinder___yellow = (8, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (8, Weapons.Smokewinder___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.GroundAttack, task.PinpointStrike, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike, task.SEAD, task.Escort, task.CAP]
    task_default = task.CAS


class KC130(PlaneType):
    id = "KC130"
    group_size_max = 1
    height = 11.66
    width = 40.4
    length = 29.79
    fuel_max = 30000
    max_speed = 621
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "KC130"  # from type

    pylons: Set[int] = set()

    tasks = [task.Refueling]
    task_default = task.Refueling


class KC135MPRS(PlaneType):
    id = "KC135MPRS"
    group_size_max = 1
    height = 12.93
    width = 40
    length = 46.61
    fuel_max = 90700
    max_speed = 1009.008
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    livery_name = "KC135MPRS"  # from type

    pylons: Set[int] = set()

    tasks = [task.Refueling]
    task_default = task.Refueling


class C_101EB(PlaneType):
    id = "C-101EB"
    flyable = True
    height = 4.25
    width = 14
    length = 12.25
    fuel_max = 1796
    max_speed = 925.2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 225

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 271,
                5: 255,
                10: 263,
                20: 285,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                19: 275,
                15: 265
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": 1,
        "MountIFRHood": False,
        "NS430allow": 1,
        "SmokeOnGround": False,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class MountIFRHood:
            id = "MountIFRHood"

        class NS430allow:
            id = "NS430allow"

            class Values:
                Not_installed = 0
                Forward_seat = 1
                Rear_seat = 2

        class SmokeOnGround:
            id = "SmokeOnGround"

    livery_name = "C-101EB"  # from type

    class Pylon1:
        Smoke_System__White_Smoke_ = (1, Weapons.Smoke_System__White_Smoke_)

    class Pylon2:
        Smoke_System_red_colorant = (2, Weapons.Smoke_System_red_colorant)
        Smoke_System_yellow_colorant = (2, Weapons.Smoke_System_yellow_colorant)

    pylons: Set[int] = {1, 2}

    tasks = [task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class C_101CC(PlaneType):
    id = "C-101CC"
    flyable = True
    height = 4.25
    width = 14
    length = 12.25
    fuel_max = 1796
    max_speed = 925.2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 225

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 271,
                5: 255,
                10: 263,
                20: 281,
                21: 285,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                19: 275,
                15: 265
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": 1,
        "MountIFRHood": False,
        "CameraRecorder": False,
        "SightSunFilter": False,
        "NS430allow": 1,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class MountIFRHood:
            id = "MountIFRHood"

        class CameraRecorder:
            id = "CameraRecorder"

        class SightSunFilter:
            id = "SightSunFilter"

        class NS430allow:
            id = "NS430allow"

            class Values:
                Not_installed = 0
                Forward_seat = 1
                Rear_seat = 2

    livery_name = "C-101CC"  # from type

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        R550_Magic_2_IR_AAM = (1, Weapons.R550_Magic_2_IR_AAM)

    class Pylon2:
        Sea_Eagle___ASM = (2, Weapons.Sea_Eagle___ASM)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (2, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        Belouga = (2, Weapons.Belouga)
        BR_250 = (2, Weapons.BR_250)
        BIN_200 = (2, Weapons.BIN_200)

    class Pylon3:
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (3, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        Belouga = (3, Weapons.Belouga)
        BR_250 = (3, Weapons.BR_250)
        BR_500 = (3, Weapons.BR_500)
        BIN_200 = (3, Weapons.BIN_200)
        CBLS_200 = (3, Weapons.CBLS_200)

    class Pylon4:
        DEFA_553___30mm_Revolver_Cannon = (4, Weapons.DEFA_553___30mm_Revolver_Cannon)
        AN_M3___2_Browning_Machine_Guns_12_7mm = (4, Weapons.AN_M3___2_Browning_Machine_Guns_12_7mm)

    class Pylon5:
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (5, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (5, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        Belouga = (5, Weapons.Belouga)
        BR_250 = (5, Weapons.BR_250)
        BR_500 = (5, Weapons.BR_500)
        BIN_200 = (5, Weapons.BIN_200)
        CBLS_200 = (5, Weapons.CBLS_200)

    class Pylon6:
        Sea_Eagle___ASM = (6, Weapons.Sea_Eagle___ASM)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (6, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (6, Weapons.LAU_131_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (6, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        Belouga = (6, Weapons.Belouga)
        BR_250 = (6, Weapons.BR_250)
        BIN_200 = (6, Weapons.BIN_200)

    class Pylon7:
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (7, Weapons.AIM_9P_Sidewinder_IR_AAM)
        R550_Magic_2_IR_AAM = (7, Weapons.R550_Magic_2_IR_AAM)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept, task.AntishipStrike, task.RunwayAttack, task.AFAC, task.Reconnaissance]
    task_default = task.CAS


class J_11A(PlaneType):
    id = "J-11A"
    flyable = True
    height = 5.932
    width = 14.7
    length = 21.935
    fuel_max = 9400
    max_speed = 2499.984
    chaff = 96
    flare = 96
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    livery_name = "J-11A"  # from type

    class Pylon1:
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        RKL609_ECM_Pod__Left_ = (1, Weapons.RKL609_ECM_Pod__Left_)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (2, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (2, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (2, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (2, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (2, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (2, Weapons.Smoke_Generator___orange)

    class Pylon3:
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (3, Weapons.R_77__AA_12_Adder____Active_Rdr)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_8M1___20_S_8OFP2 = (3, Weapons.B_8M1___20_S_8OFP2)
        _2_x_FAB_250 = (3, Weapons._2_x_FAB_250)
        _2_x_FAB_500 = (3, Weapons._2_x_FAB_500)
        _2_x_RBK_250_PTAB_2_5M = (3, Weapons._2_x_RBK_250_PTAB_2_5M)
        _2_x_RBK_500_255_PTAB_10_5 = (3, Weapons._2_x_RBK_500_255_PTAB_10_5)
        _2_x_B_13L___5_S_13_OF = (3, Weapons._2_x_B_13L___5_S_13_OF)
        _2_x_B_8M1___20_S_8KOM = (3, Weapons._2_x_B_8M1___20_S_8KOM)
        _2_x_B_8M1___20_S_8TsM = (3, Weapons._2_x_B_8M1___20_S_8TsM)
        _2_x_B_8M1___20_S_8OFP2 = (3, Weapons._2_x_B_8M1___20_S_8OFP2)
        _2_x_S_25 = (3, Weapons._2_x_S_25)

    class Pylon4:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (4, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (4, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (4, Weapons.R_77__AA_12_Adder____Active_Rdr)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon5:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (5, Weapons.R_77__AA_12_Adder____Active_Rdr)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    class Pylon6:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (6, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (6, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (6, Weapons.R_77__AA_12_Adder____Active_Rdr)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)

    class Pylon7:
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (7, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (7, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (7, Weapons.R_77__AA_12_Adder____Active_Rdr)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)

    class Pylon8:
        R_73__AA_11_Archer____Infra_Red = (8, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (8, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (8, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (8, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (8, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        R_77__AA_12_Adder____Active_Rdr = (8, Weapons.R_77__AA_12_Adder____Active_Rdr)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (8, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (8, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (8, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (8, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_8M1___20_S_8OFP2 = (8, Weapons.B_8M1___20_S_8OFP2)
        _2_x_FAB_250_ = (8, Weapons._2_x_FAB_250_)
        _2_x_FAB_500_ = (8, Weapons._2_x_FAB_500_)
        _2_x_RBK_250_PTAB_2_5M_ = (8, Weapons._2_x_RBK_250_PTAB_2_5M_)
        _2_x_RBK_500_255_PTAB_10_5_ = (8, Weapons._2_x_RBK_500_255_PTAB_10_5_)
        _2_x_B_13L___5_S_13_OF_ = (8, Weapons._2_x_B_13L___5_S_13_OF_)
        _2_x_B_8M1___20_S_8KOM_ = (8, Weapons._2_x_B_8M1___20_S_8KOM_)
        _2_x_B_8M1___20_S_8TsM_ = (8, Weapons._2_x_B_8M1___20_S_8TsM_)
        _2_x_B_8M1___20_S_8OFP2_ = (8, Weapons._2_x_B_8M1___20_S_8OFP2_)
        _2_x_S_25_ = (8, Weapons._2_x_S_25_)

    class Pylon9:
        R_73__AA_11_Archer____Infra_Red = (9, Weapons.R_73__AA_11_Archer____Infra_Red)
        Smoke_Generator___red = (9, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (9, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (9, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (9, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (9, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (9, Weapons.Smoke_Generator___orange)

    class Pylon10:
        R_73__AA_11_Archer____Infra_Red = (10, Weapons.R_73__AA_11_Archer____Infra_Red)
        RKL609_ECM_Pod__Right_ = (10, Weapons.RKL609_ECM_Pod__Right_)
        Smoke_Generator___red = (10, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (10, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (10, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (10, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (10, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (10, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Intercept, task.Escort, task.FighterSweep, task.AFAC, task.CAS, task.GroundAttack, task.RunwayAttack, task.AntishipStrike]
    task_default = task.CAP


class JF_17(PlaneType):
    id = "JF-17"
    flyable = True
    height = 4.7
    width = 8.5
    length = 14.25
    fuel_max = 2325
    max_speed = 2520
    chaff = 36
    flare = 32
    charge_total = 68
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 243

    panel_radio = {
        1: {
            "channels": {
                1: 108,
                2: 108.5,
                4: 109.5,
                8: 111.5,
                16: 115.5,
                17: 116,
                9: 112,
                18: 116.5,
                5: 110,
                10: 112.5,
                20: 117.5,
                11: 113,
                3: 109,
                6: 110.5,
                12: 113.5,
                13: 114,
                7: 111,
                14: 114.5,
                19: 117,
                15: 115
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "LaserCode100": 6,
        "LaserCode10": 8,
        "LaserCode1": 8,
        "AARProbe": False,
    }

    class Properties:

        class LaserCode100:
            id = "LaserCode100"

        class LaserCode10:
            id = "LaserCode10"

        class LaserCode1:
            id = "LaserCode1"

        class AARProbe:
            id = "AARProbe"

    livery_name = "JF-17"  # from type

    class Pylon1:
        DIS_PL_5EII = (1, Weapons.DIS_PL_5EII)
        DIS_SMOKE_GENERATOR_R = (1, Weapons.DIS_SMOKE_GENERATOR_R)
        DIS_SMOKE_GENERATOR_G = (1, Weapons.DIS_SMOKE_GENERATOR_G)
        DIS_SMOKE_GENERATOR_B = (1, Weapons.DIS_SMOKE_GENERATOR_B)
        DIS_SMOKE_GENERATOR_W = (1, Weapons.DIS_SMOKE_GENERATOR_W)
        DIS_SMOKE_GENERATOR_Y = (1, Weapons.DIS_SMOKE_GENERATOR_Y)
        DIS_SMOKE_GENERATOR_O = (1, Weapons.DIS_SMOKE_GENERATOR_O)

    class Pylon2:
        DIS_PL_5EII = (2, Weapons.DIS_PL_5EII)
        DIS_SD_10 = (2, Weapons.DIS_SD_10)
        DIS_SD_10_DUAL_L = (2, Weapons.DIS_SD_10_DUAL_L)
        DIS_LD_10 = (2, Weapons.DIS_LD_10)
        DIS_LD_10_DUAL_L = (2, Weapons.DIS_LD_10_DUAL_L)
        DIS_C_701T = (2, Weapons.DIS_C_701T)
        DIS_C_701IR = (2, Weapons.DIS_C_701IR)
        DIS_LS_6_500 = (2, Weapons.DIS_LS_6_500)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        DIS_MK_20 = (2, Weapons.DIS_MK_20)
        DIS_GBU_12 = (2, Weapons.DIS_GBU_12)
        DIS_TYPE200 = (2, Weapons.DIS_TYPE200)
        DIS_TYPE200_DUAL_L = (2, Weapons.DIS_TYPE200_DUAL_L)
        DIS_MK_82_DUAL_GDJ_II19_L = (2, Weapons.DIS_MK_82_DUAL_GDJ_II19_L)
        DIS_MK_82S_DUAL_GDJ_II19_L = (2, Weapons.DIS_MK_82S_DUAL_GDJ_II19_L)
        DIS_MK_20_DUAL_GDJ_II19_L = (2, Weapons.DIS_MK_20_DUAL_GDJ_II19_L)
        DIS_GBU_12_DUAL_GDJ_II19_L = (2, Weapons.DIS_GBU_12_DUAL_GDJ_II19_L)
        DIS_BRM1_90 = (2, Weapons.DIS_BRM1_90)
        DIS_RKT_90_UG = (2, Weapons.DIS_RKT_90_UG)
        DIS_LAU68_MK5_DUAL_GDJ_II19_L = (2, Weapons.DIS_LAU68_MK5_DUAL_GDJ_II19_L)
        DIS_WMD7 = (2, Weapons.DIS_WMD7)
        DIS_AKG_DLPOD = (2, Weapons.DIS_AKG_DLPOD)
        DIS_SMOKE_GENERATOR_R = (2, Weapons.DIS_SMOKE_GENERATOR_R)
        DIS_SMOKE_GENERATOR_G = (2, Weapons.DIS_SMOKE_GENERATOR_G)
        DIS_SMOKE_GENERATOR_B = (2, Weapons.DIS_SMOKE_GENERATOR_B)
        DIS_SMOKE_GENERATOR_W = (2, Weapons.DIS_SMOKE_GENERATOR_W)
        DIS_SMOKE_GENERATOR_Y = (2, Weapons.DIS_SMOKE_GENERATOR_Y)
        DIS_SMOKE_GENERATOR_O = (2, Weapons.DIS_SMOKE_GENERATOR_O)

    class Pylon3:
        DIS_C_802AK = (3, Weapons.DIS_C_802AK)
        DIS_CM_802AKG = (3, Weapons.DIS_CM_802AKG)
        DIS_CM_802AKG_AI = (3, Weapons.DIS_CM_802AKG_AI)
        DIS_LS_6_500 = (3, Weapons.DIS_LS_6_500)
        DIS_GB6 = (3, Weapons.DIS_GB6)
        DIS_GB6_TSP = (3, Weapons.DIS_GB6_TSP)
        DIS_GB6_HE = (3, Weapons.DIS_GB6_HE)
        DIS_TANK800 = (3, Weapons.DIS_TANK800)
        DIS_TANK1100 = (3, Weapons.DIS_TANK1100)
        DIS_TANK800_EMPTY = (3, Weapons.DIS_TANK800_EMPTY)
        DIS_TANK1100_EMPTY = (3, Weapons.DIS_TANK1100_EMPTY)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        DIS_MK_20 = (3, Weapons.DIS_MK_20)
        DIS_GBU_10 = (3, Weapons.DIS_GBU_10)
        DIS_GBU_16 = (3, Weapons.DIS_GBU_16)
        DIS_GBU_12 = (3, Weapons.DIS_GBU_12)
        DIS_TYPE200 = (3, Weapons.DIS_TYPE200)

    class Pylon4:
        DIS_TANK800 = (4, Weapons.DIS_TANK800)
        DIS_TANK800_EMPTY = (4, Weapons.DIS_TANK800_EMPTY)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        DIS_GBU_10 = (4, Weapons.DIS_GBU_10)
        DIS_GBU_16 = (4, Weapons.DIS_GBU_16)
        DIS_WMD7 = (4, Weapons.DIS_WMD7)
        DIS_AKG_DLPOD = (4, Weapons.DIS_AKG_DLPOD)
        DIS_SPJ_POD = (4, Weapons.DIS_SPJ_POD)
        DIS_SMOKE_GENERATOR_R = (4, Weapons.DIS_SMOKE_GENERATOR_R)
        DIS_SMOKE_GENERATOR_G = (4, Weapons.DIS_SMOKE_GENERATOR_G)
        DIS_SMOKE_GENERATOR_B = (4, Weapons.DIS_SMOKE_GENERATOR_B)
        DIS_SMOKE_GENERATOR_W = (4, Weapons.DIS_SMOKE_GENERATOR_W)
        DIS_SMOKE_GENERATOR_Y = (4, Weapons.DIS_SMOKE_GENERATOR_Y)
        DIS_SMOKE_GENERATOR_O = (4, Weapons.DIS_SMOKE_GENERATOR_O)

    class Pylon5:
        DIS_C_802AK = (5, Weapons.DIS_C_802AK)
        DIS_CM_802AKG = (5, Weapons.DIS_CM_802AKG)
        DIS_CM_802AKG_AI = (5, Weapons.DIS_CM_802AKG_AI)
        DIS_LS_6_500 = (5, Weapons.DIS_LS_6_500)
        DIS_GB6 = (5, Weapons.DIS_GB6)
        DIS_GB6_TSP = (5, Weapons.DIS_GB6_TSP)
        DIS_GB6_HE = (5, Weapons.DIS_GB6_HE)
        DIS_TANK800 = (5, Weapons.DIS_TANK800)
        DIS_TANK1100 = (5, Weapons.DIS_TANK1100)
        DIS_TANK800_EMPTY = (5, Weapons.DIS_TANK800_EMPTY)
        DIS_TANK1100_EMPTY = (5, Weapons.DIS_TANK1100_EMPTY)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        DIS_MK_20 = (5, Weapons.DIS_MK_20)
        DIS_GBU_10 = (5, Weapons.DIS_GBU_10)
        DIS_GBU_16 = (5, Weapons.DIS_GBU_16)
        DIS_GBU_12 = (5, Weapons.DIS_GBU_12)
        DIS_TYPE200 = (5, Weapons.DIS_TYPE200)

    class Pylon6:
        DIS_PL_5EII = (6, Weapons.DIS_PL_5EII)
        DIS_SD_10 = (6, Weapons.DIS_SD_10)
        DIS_SD_10_DUAL_R = (6, Weapons.DIS_SD_10_DUAL_R)
        DIS_LD_10 = (6, Weapons.DIS_LD_10)
        DIS_LD_10_DUAL_R = (6, Weapons.DIS_LD_10_DUAL_R)
        DIS_C_701T = (6, Weapons.DIS_C_701T)
        DIS_C_701IR = (6, Weapons.DIS_C_701IR)
        DIS_LS_6_500 = (6, Weapons.DIS_LS_6_500)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        DIS_MK_20 = (6, Weapons.DIS_MK_20)
        DIS_GBU_12 = (6, Weapons.DIS_GBU_12)
        DIS_TYPE200 = (6, Weapons.DIS_TYPE200)
        DIS_TYPE200_DUAL_R = (6, Weapons.DIS_TYPE200_DUAL_R)
        DIS_MK_82_DUAL_GDJ_II19_R = (6, Weapons.DIS_MK_82_DUAL_GDJ_II19_R)
        DIS_MK_82S_DUAL_GDJ_II19_R = (6, Weapons.DIS_MK_82S_DUAL_GDJ_II19_R)
        DIS_MK_20_DUAL_GDJ_II19_R = (6, Weapons.DIS_MK_20_DUAL_GDJ_II19_R)
        DIS_GBU_12_DUAL_GDJ_II19_R = (6, Weapons.DIS_GBU_12_DUAL_GDJ_II19_R)
        DIS_BRM1_90 = (6, Weapons.DIS_BRM1_90)
        DIS_RKT_90_UG = (6, Weapons.DIS_RKT_90_UG)
        DIS_LAU68_MK5_DUAL_GDJ_II19_R = (6, Weapons.DIS_LAU68_MK5_DUAL_GDJ_II19_R)
        DIS_WMD7 = (6, Weapons.DIS_WMD7)
        DIS_AKG_DLPOD = (6, Weapons.DIS_AKG_DLPOD)
        DIS_SMOKE_GENERATOR_R = (6, Weapons.DIS_SMOKE_GENERATOR_R)
        DIS_SMOKE_GENERATOR_G = (6, Weapons.DIS_SMOKE_GENERATOR_G)
        DIS_SMOKE_GENERATOR_B = (6, Weapons.DIS_SMOKE_GENERATOR_B)
        DIS_SMOKE_GENERATOR_W = (6, Weapons.DIS_SMOKE_GENERATOR_W)
        DIS_SMOKE_GENERATOR_Y = (6, Weapons.DIS_SMOKE_GENERATOR_Y)
        DIS_SMOKE_GENERATOR_O = (6, Weapons.DIS_SMOKE_GENERATOR_O)

    class Pylon7:
        DIS_PL_5EII = (7, Weapons.DIS_PL_5EII)
        DIS_SMOKE_GENERATOR_R = (7, Weapons.DIS_SMOKE_GENERATOR_R)
        DIS_SMOKE_GENERATOR_G = (7, Weapons.DIS_SMOKE_GENERATOR_G)
        DIS_SMOKE_GENERATOR_B = (7, Weapons.DIS_SMOKE_GENERATOR_B)
        DIS_SMOKE_GENERATOR_W = (7, Weapons.DIS_SMOKE_GENERATOR_W)
        DIS_SMOKE_GENERATOR_Y = (7, Weapons.DIS_SMOKE_GENERATOR_Y)
        DIS_SMOKE_GENERATOR_O = (7, Weapons.DIS_SMOKE_GENERATOR_O)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.Intercept, task.CAP, task.AFAC, task.Reconnaissance, task.Escort, task.FighterSweep, task.SEAD, task.AntishipStrike, task.CAS, task.GroundAttack, task.PinpointStrike, task.RunwayAttack]
    task_default = task.CAP


class KJ_2000(PlaneType):
    id = "KJ-2000"
    group_size_max = 1
    height = 14.76
    width = 50.5
    length = 46.59
    fuel_max = 70000
    max_speed = 849.996
    category = "AWACS"  #{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}

    livery_name = "KJ-2000"  # from type

    pylons: Set[int] = set()

    tasks = [task.AWACS]
    task_default = task.AWACS


class WingLoong_I(PlaneType):
    id = "WingLoong-I"
    group_size_max = 1
    height = 2.77
    width = 14
    length = 9.05
    fuel_max = 400
    max_speed = 280
    eplrs = True
    radio_frequency = 127.5

    livery_name = "WINGLOONG-I"  # from type

    class Pylon1:
        DIS_AKD_10 = (1, Weapons.DIS_AKD_10)

    class Pylon2:
        DIS_AKD_10 = (2, Weapons.DIS_AKD_10)

    pylons: Set[int] = {1, 2}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Reconnaissance]
    task_default = task.CAS


class H_6J(PlaneType):
    id = "H-6J"
    height = 10.36
    width = 33
    length = 34.8
    fuel_max = 25000
    max_speed = 1044
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True

    property_defaults: Dict[str, Any] = {
        "Belly_Bay_Door": False,
    }

    class Properties:

        class Belly_Bay_Door:
            id = "Belly Bay Door"

    livery_name = "H-6J"  # from type

    class Pylon1:
        DIS_GDJ_YJ83K = (1, Weapons.DIS_GDJ_YJ83K)
        DIS_DF4A_KD20 = (1, Weapons.DIS_DF4A_KD20)
        DIS_MER6_250_2_N6 = (1, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (1, Weapons.DIS_MER6_250_3_N6)

    class Pylon2:
        DIS_GDJ_KD63 = (2, Weapons.DIS_GDJ_KD63)
        DIS_GDJ_KD63B = (2, Weapons.DIS_GDJ_KD63B)
        DIS_DF4B_YJ12 = (2, Weapons.DIS_DF4B_YJ12)
        DIS_DF4A_KD20 = (2, Weapons.DIS_DF4A_KD20)
        DIS_GDJ_YJ83K = (2, Weapons.DIS_GDJ_YJ83K)
        DIS_MER6_250_2_N6 = (2, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (2, Weapons.DIS_MER6_250_3_N6)

    class Pylon3:
        DIS_GDJ_KD63 = (3, Weapons.DIS_GDJ_KD63)
        DIS_GDJ_KD63B = (3, Weapons.DIS_GDJ_KD63B)
        DIS_DF4B_YJ12 = (3, Weapons.DIS_DF4B_YJ12)
        DIS_DF4A_KD20 = (3, Weapons.DIS_DF4A_KD20)
        DIS_GDJ_YJ83K = (3, Weapons.DIS_GDJ_YJ83K)
        DIS_MER6_250_2_N6 = (3, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (3, Weapons.DIS_MER6_250_3_N6)

    class Pylon4:
        DIS_GDJ_KD63 = (4, Weapons.DIS_GDJ_KD63)
        DIS_GDJ_KD63B = (4, Weapons.DIS_GDJ_KD63B)
        DIS_DF4B_YJ12 = (4, Weapons.DIS_DF4B_YJ12)
        DIS_DF4A_KD20 = (4, Weapons.DIS_DF4A_KD20)
        DIS_GDJ_YJ83K = (4, Weapons.DIS_GDJ_YJ83K)
        DIS_MER6_250_2_N6 = (4, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (4, Weapons.DIS_MER6_250_3_N6)

    class Pylon5:
        DIS_GDJ_KD63 = (5, Weapons.DIS_GDJ_KD63)
        DIS_GDJ_KD63B = (5, Weapons.DIS_GDJ_KD63B)
        DIS_DF4B_YJ12 = (5, Weapons.DIS_DF4B_YJ12)
        DIS_DF4A_KD20 = (5, Weapons.DIS_DF4A_KD20)
        DIS_GDJ_YJ83K = (5, Weapons.DIS_GDJ_YJ83K)
        DIS_MER6_250_2_N6 = (5, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (5, Weapons.DIS_MER6_250_3_N6)

    class Pylon6:
        DIS_GDJ_YJ83K = (6, Weapons.DIS_GDJ_YJ83K)
        DIS_DF4A_KD20 = (6, Weapons.DIS_DF4A_KD20)
        DIS_MER6_250_2_N6 = (6, Weapons.DIS_MER6_250_2_N6)
        DIS_MER6_250_3_N6 = (6, Weapons.DIS_MER6_250_3_N6)

    class Pylon7:
        DIS_AKG_DLPOD = (7, Weapons.DIS_AKG_DLPOD)

    class Pylon8:
        DIS_H6_250_2_N24 = (8, Weapons.DIS_H6_250_2_N24)
        DIS_H6_250_2_N12 = (8, Weapons.DIS_H6_250_2_N12)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.AntishipStrike, task.GroundAttack, task.PinpointStrike, task.RunwayAttack, task.CAS]
    task_default = task.AntishipStrike


class Christen_Eagle_II(PlaneType):
    id = "Christen Eagle II"
    height = 1.9812
    width = 11.594846
    length = 5.6388
    fuel_max = 71
    max_speed = 306
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": 1,
        "NS430allow": True,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class NS430allow:
            id = "NS430allow"

    livery_name = "CHRISTEN EAGLE II"  # from type

    class Pylon1:
        Smoke_for_Christen_Eagle_II__white = (1, Weapons.Smoke_for_Christen_Eagle_II__white)

    pylons: Set[int] = {1}

    tasks = [task.Transport, task.Reconnaissance]
    task_default = task.Nothing


class F_16C_50(PlaneType):
    id = "F-16C_50"
    flyable = True
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 3249
    max_speed = 2120.04
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
        2: {
            "channels": {
                1: 127,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 139,
                13: 140,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
    }

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Viper",
            "Venom",
            "Lobo",
            "Cowboy",
            "Python",
            "Rattler",
            "Panther",
            "Wolf",
            "Weasel",
            "Wild",
            "Ninja",
            "Jedi",
        ]
    }

    property_defaults: Dict[str, Any] = {
        "LAU3ROF": 0,
        "LaserCode100": 6,
        "LaserCode10": 8,
        "LaserCode1": 8,
        "HelmetMountedDevice": 1,
    }

    class Properties:

        class LAU3ROF:
            id = "LAU3ROF"

            class Values:
                Single = 0
                Ripple = 1

        class LaserCode100:
            id = "LaserCode100"

        class LaserCode10:
            id = "LaserCode10"

        class LaserCode1:
            id = "LaserCode1"

        class HelmetMountedDevice:
            id = "HelmetMountedDevice"

            class Values:
                Not_installed = 0
                JHMCS = 1
                NVG = 2

    livery_name = "F-16C_50"  # from type

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (1, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (2, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (2, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
#ERRR <CLEAN>

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (3, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (3, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU3_WP1B = (3, Weapons.LAU3_WP1B)
        LAU3_WP61 = (3, Weapons.LAU3_WP61)
        LAU3_HE5 = (3, Weapons.LAU3_HE5)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        BRU_57_with_2_x_CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.BRU_57_with_2_x_CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BRU_57_with_2_x_CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.BRU_57_with_2_x_CBU_103___202_x_CEM__CBU_with_WCMD)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (3, Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (3, Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (3, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (3, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H = (3, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_3 = (3, Weapons.LAU_88_AGM_65H_3)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_57_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.BRU_57_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154A___JSOW_CEB__CBU_type_ = (3, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        BRU_57_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (3, Weapons.BRU_57_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        ALQ_184 = (3, Weapons.ALQ_184)
        ALQ_184_Long = (3, Weapons.ALQ_184_Long)
#ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (3, Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb)
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb)
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H_2_L = (3, Weapons.LAU_88_AGM_65H_2_L)

    class Pylon4:
        LAU3_WP156 = (4, Weapons.LAU3_WP156)
        LAU3_WP1B = (4, Weapons.LAU3_WP1B)
        LAU3_WP61 = (4, Weapons.LAU3_WP61)
        LAU3_HE5 = (4, Weapons.LAU3_HE5)
        LAU3_HE151 = (4, Weapons.LAU3_HE151)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (4, Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (4, Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb)
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (4, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        MXU_648_TP = (4, Weapons.MXU_648_TP)
#ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (4, Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb)
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb)

    class Pylon5:
        Fuel_tank_300_gal = (5, Weapons.Fuel_tank_300_gal)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        ALQ_184 = (5, Weapons.ALQ_184)
        ALQ_184_Long = (5, Weapons.ALQ_184_Long)
#ERRR <CLEAN>

    class Pylon6:
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU3_WP1B = (6, Weapons.LAU3_WP1B)
        LAU3_WP61 = (6, Weapons.LAU3_WP61)
        LAU3_HE5 = (6, Weapons.LAU3_HE5)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (6, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (6, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (6, Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (6, Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb)
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (6, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Fuel_tank_370_gal = (6, Weapons.Fuel_tank_370_gal)
        MXU_648_TP = (6, Weapons.MXU_648_TP)
#ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (6, Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_)
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (6, Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_)
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (6, Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_)
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (6, Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_)
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (6, Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_)

    class Pylon7:
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (7, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (7, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (7, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (7, Weapons.LAU3_WP156)
        LAU3_WP1B = (7, Weapons.LAU3_WP1B)
        LAU3_WP61 = (7, Weapons.LAU3_WP61)
        LAU3_HE5 = (7, Weapons.LAU3_HE5)
        LAU3_HE151 = (7, Weapons.LAU3_HE151)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (7, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (7, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        BRU_57_with_2_x_CBU_105___10_x_SFW__CBU_with_WCMD = (7, Weapons.BRU_57_with_2_x_CBU_105___10_x_SFW__CBU_with_WCMD)
        CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        BRU_57_with_2_x_CBU_103___202_x_CEM__CBU_with_WCMD = (7, Weapons.BRU_57_with_2_x_CBU_103___202_x_CEM__CBU_with_WCMD)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (7, Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (7, Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_AGM_65G = (7, Weapons.LAU_117_AGM_65G)
        LAU_117_AGM_65H = (7, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (7, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_88_AGM_65D_ONE = (7, Weapons.LAU_88_AGM_65D_ONE)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (7, Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_88_AGM_65H = (7, Weapons.LAU_88_AGM_65H)
        LAU_88_AGM_65H_3 = (7, Weapons.LAU_88_AGM_65H_3)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (7, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_57_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.BRU_57_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154A___JSOW_CEB__CBU_type_ = (7, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        BRU_57_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (7, Weapons.BRU_57_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        MXU_648_TP = (7, Weapons.MXU_648_TP)
        ALQ_184 = (7, Weapons.ALQ_184)
        ALQ_184_Long = (7, Weapons.ALQ_184_Long)
#ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (7, Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_)
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (7, Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_)
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (7, Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_)
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_ = (7, Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_)
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (7, Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_)
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (7, Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_)
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__ = (7, Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM__)
        LAU_88_AGM_65H_2_R = (7, Weapons.LAU_88_AGM_65H_2_R)

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (8, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (8, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (8, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
#ERRR <CLEAN>

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (9, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        CATM_9M = (9, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon10:
        AN_ASQ_213_HTS___HARM_Targeting_System = (10, Weapons.AN_ASQ_213_HTS___HARM_Targeting_System)

    class Pylon11:
        AN_AAQ_28_LITENING___Targeting_Pod = (11, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class F_5E(PlaneType):
    id = "F-5E"
    height = 4.06
    width = 8.53
    length = 14.68
    fuel_max = 1996
    max_speed = 1742.4
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    livery_name = "F-5E"  # from type

    class Pylon1:
        AIM_9B_Sidewinder_IR_AAM = (1, Weapons.AIM_9B_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (1, Weapons.CATM_9M)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        M117___750lb_GP_Bomb_LD = (2, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (2, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (2, Weapons.LAU3_WP156)
        LAU3_WP1B = (2, Weapons.LAU3_WP1B)
        LAU3_WP61 = (2, Weapons.LAU3_WP61)
        LAU3_HE5 = (2, Weapons.LAU3_HE5)
        LAU3_HE151 = (2, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BDU_33___25lb_Practice_Bomb_LD = (2, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (2, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon3:
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (3, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (3, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU3_WP1B = (3, Weapons.LAU3_WP1B)
        LAU3_WP61 = (3, Weapons.LAU3_WP61)
        LAU3_HE5 = (3, Weapons.LAU3_HE5)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        F_5_275Gal_Fuel_tank = (3, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (3, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (3, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (4, Weapons.M117___750lb_GP_Bomb_LD)
        _5_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons._5_x_Mk_82___500lb_GP_Bombs_LD)
        _5_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons._5_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        CBU_52B___220_x_HE_Frag_bomblets = (4, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        F_5_275Gal_Fuel_tank = (4, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (4, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (4, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (4, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (5, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (5, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (5, Weapons.LAU3_WP156)
        LAU3_WP1B = (5, Weapons.LAU3_WP1B)
        LAU3_WP61 = (5, Weapons.LAU3_WP61)
        LAU3_HE5 = (5, Weapons.LAU3_HE5)
        LAU3_HE151 = (5, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        F_5_275Gal_Fuel_tank = (5, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (5, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (5, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (5, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        M117___750lb_GP_Bomb_LD = (6, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (6, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU3_WP1B = (6, Weapons.LAU3_WP1B)
        LAU3_WP61 = (6, Weapons.LAU3_WP61)
        LAU3_HE5 = (6, Weapons.LAU3_HE5)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (6, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BDU_33___25lb_Practice_Bomb_LD = (6, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon7:
        AIM_9B_Sidewinder_IR_AAM = (7, Weapons.AIM_9B_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (7, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (7, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (7, Weapons.CATM_9M)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AntishipStrike]
    task_default = task.CAP


class F_5E_3(PlaneType):
    id = "F-5E-3"
    flyable = True
    height = 4.06
    width = 8.53
    length = 14.68
    fuel_max = 2046
    max_speed = 1742.4
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "LAU3ROF": 0,
        "LAU68ROF": 0,
        "LaserCode100": 6,
        "LaserCode10": 8,
        "LaserCode1": 8,
        "ChaffBurst": 0,
        "ChaffSalvo": 0,
        "ChaffBurstInt": 0,
        "ChaffSalvoInt": 0,
        "FlareBurst": 0,
        "FlareBurstInt": 0,
    }

    class Properties:

        class LAU3ROF:
            id = "LAU3ROF"

            class Values:
                Single = 0
                Ripple__17ms = 1
                Ripple__20ms = 2
                Ripple__60ms = 3

        class LAU68ROF:
            id = "LAU68ROF"

            class Values:
                Single = 0
                Ripple__60ms = 1

        class LaserCode100:
            id = "LaserCode100"

        class LaserCode10:
            id = "LaserCode10"

        class LaserCode1:
            id = "LaserCode1"

        class ChaffBurst:
            id = "ChaffBurst"

            class Values:
                _1 = 0
                _2 = 1
                _3 = 2
                _4 = 3
                _6 = 4
                _8 = 5

        class ChaffSalvo:
            id = "ChaffSalvo"

            class Values:
                _1 = 0
                _2 = 1
                _4 = 2
                _8 = 3
                C = 4

        class ChaffBurstInt:
            id = "ChaffBurstInt"

            class Values:
                _0_1s = 0
                _0_2s = 1
                _0_3s = 2
                _0_4s = 3

        class ChaffSalvoInt:
            id = "ChaffSalvoInt"

            class Values:
                _1s = 0
                _2s = 1
                _3s = 2
                _4s = 3
                _5s = 4
                _8s = 5
                R = 6

        class FlareBurst:
            id = "FlareBurst"

            class Values:
                _1 = 0
                _2 = 1
                _4 = 2
                _8 = 3
                C = 4

        class FlareBurstInt:
            id = "FlareBurstInt"

            class Values:
                _3s = 0
                _4s = 1
                _6s = 2
                _8s = 3
                _10s = 4

    livery_name = "F-5E-3"  # from livery_entry

    class Pylon1:
        AIM_9B_Sidewinder_IR_AAM = (1, Weapons.AIM_9B_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (1, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (1, Weapons.CATM_9M)

    class Pylon2:
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        M117___750lb_GP_Bomb_LD = (2, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (2, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (2, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (2, Weapons.LAU3_WP156)
        LAU3_WP1B = (2, Weapons.LAU3_WP1B)
        LAU3_WP61 = (2, Weapons.LAU3_WP61)
        LAU3_HE5 = (2, Weapons.LAU3_HE5)
        LAU3_HE151 = (2, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (2, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (2, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BDU_33___25lb_Practice_Bomb_LD = (2, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (2, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (2, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon3:
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (3, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (3, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (3, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU3_WP1B = (3, Weapons.LAU3_WP1B)
        LAU3_WP61 = (3, Weapons.LAU3_WP61)
        LAU3_HE5 = (3, Weapons.LAU3_HE5)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (3, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        F_5_275Gal_Fuel_tank = (3, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (3, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (3, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (3, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (3, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (3, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (4, Weapons.M117___750lb_GP_Bomb_LD)
        _5_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons._5_x_Mk_82___500lb_GP_Bombs_LD)
        _5_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons._5_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        CBU_52B___220_x_HE_Frag_bomblets = (4, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        F_5_275Gal_Fuel_tank = (4, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (4, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (4, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (4, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (4, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (4, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (5, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (5, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (5, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (5, Weapons.LAU3_WP156)
        LAU3_WP1B = (5, Weapons.LAU3_WP1B)
        LAU3_WP61 = (5, Weapons.LAU3_WP61)
        LAU3_HE5 = (5, Weapons.LAU3_HE5)
        LAU3_HE151 = (5, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (5, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        F_5_275Gal_Fuel_tank = (5, Weapons.F_5_275Gal_Fuel_tank)
        F_5_150Gal_Fuel_tank = (5, Weapons.F_5_150Gal_Fuel_tank)
        MXU_648_TP = (5, Weapons.MXU_648_TP)
        BDU_33___25lb_Practice_Bomb_LD = (5, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (5, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (5, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        M117___750lb_GP_Bomb_LD = (6, Weapons.M117___750lb_GP_Bomb_LD)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_52B___220_x_HE_Frag_bomblets = (6, Weapons.CBU_52B___220_x_HE_Frag_bomblets)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk1__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk61__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M257__Para_Illum)
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (6, Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU3_WP1B = (6, Weapons.LAU3_WP1B)
        LAU3_WP61 = (6, Weapons.LAU3_WP61)
        LAU3_HE5 = (6, Weapons.LAU3_HE5)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_M156__Wht_Phos)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (6, Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT)
        SUU_25_x_8_LUU_2___Target_Marker_Flares = (6, Weapons.SUU_25_x_8_LUU_2___Target_Marker_Flares)
        BDU_33___25lb_Practice_Bomb_LD = (6, Weapons.BDU_33___25lb_Practice_Bomb_LD)
        BDU_50LD___500lb_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LD___500lb_Inert_Practice_Bomb_LD)
        BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD = (6, Weapons.BDU_50LGB___500lb_Laser_Guided_Inert_Practice_Bomb_LD)
        BDU_50HD___500lb_Inert_Practice_Bomb_HD = (6, Weapons.BDU_50HD___500lb_Inert_Practice_Bomb_HD)

    class Pylon7:
        AIM_9B_Sidewinder_IR_AAM = (7, Weapons.AIM_9B_Sidewinder_IR_AAM)
        AIM_9P5_Sidewinder_IR_AAM = (7, Weapons.AIM_9P5_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (7, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (7, Weapons.Smokewinder___red)
        Smokewinder___green = (7, Weapons.Smokewinder___green)
        Smokewinder___blue = (7, Weapons.Smokewinder___blue)
        Smokewinder___white = (7, Weapons.Smokewinder___white)
        Smokewinder___yellow = (7, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (7, Weapons.Smokewinder___orange)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        CATM_9M = (7, Weapons.CATM_9M)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.AntishipStrike]
    task_default = task.CAP


class F_86F_Sabre(PlaneType):
    id = "F-86F Sabre"
    flyable = True
    height = 4.496
    width = 11.9
    length = 11.43
    fuel_max = 1282
    max_speed = 964.8
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 225

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    livery_name = "F-86F SABRE"  # from livery_entry

    class Pylon1:
        Fuel_Tank_200_gallons = (1, Weapons.Fuel_Tank_200_gallons)
        Fuel_Tank_120_gallons = (1, Weapons.Fuel_Tank_120_gallons)
        _2_x_HVAR__UnGd_Rkts = (1, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (1, Weapons.HVAR_SMOKE__UnGd_Rkt)

    class Pylon2:
        _2_x_HVAR__UnGd_Rkts = (2, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (2, Weapons.HVAR_SMOKE__UnGd_Rkt)

    class Pylon3:
        _2_x_HVAR__UnGd_Rkts = (3, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (3, Weapons.HVAR_SMOKE__UnGd_Rkt)

    class Pylon4:
        Fuel_Tank_120_gallons = (4, Weapons.Fuel_Tank_120_gallons)
        AN_M64___500lb_GP_Bomb_LD_ = (4, Weapons.AN_M64___500lb_GP_Bomb_LD_)
        _2_x_HVAR__UnGd_Rkts = (4, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (4, Weapons.HVAR_SMOKE__UnGd_Rkt)
        M117___750lb_GP_Bomb_LD = (4, Weapons.M117___750lb_GP_Bomb_LD)

    class Pylon5:
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (5, Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM)

    class Pylon6:
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (6, Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM)

    class Pylon7:
        Fuel_Tank_120_gallons = (7, Weapons.Fuel_Tank_120_gallons)
        AN_M64___500lb_GP_Bomb_LD_ = (7, Weapons.AN_M64___500lb_GP_Bomb_LD_)
        _2_x_HVAR__UnGd_Rkts = (7, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (7, Weapons.HVAR_SMOKE__UnGd_Rkt)
        M117___750lb_GP_Bomb_LD = (7, Weapons.M117___750lb_GP_Bomb_LD)

    class Pylon8:
        _2_x_HVAR__UnGd_Rkts = (8, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (8, Weapons.HVAR_SMOKE__UnGd_Rkt)

    class Pylon9:
        _2_x_HVAR__UnGd_Rkts = (9, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (9, Weapons.HVAR_SMOKE__UnGd_Rkt)

    class Pylon10:
        Fuel_Tank_200_gallons = (10, Weapons.Fuel_Tank_200_gallons)
        Fuel_Tank_120_gallons = (10, Weapons.Fuel_Tank_120_gallons)
        _2_x_HVAR__UnGd_Rkts = (10, Weapons._2_x_HVAR__UnGd_Rkts)
        HVAR_SMOKE__UnGd_Rkt = (10, Weapons.HVAR_SMOKE__UnGd_Rkt)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept, task.AntishipStrike]
    task_default = task.CAP


class F_14B(PlaneType):
    id = "F-14B"
    flyable = True
    height = 4.8
    width = 10.15
    length = 16.6
    fuel_max = 7348
    max_speed = 2520
    chaff = 140
    flare = 60
    charge_total = 200
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                20: 269,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                19: 268,
                15: 265
            },
        },
        2: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                20: 269,
                30: 263,
                21: 225,
                11: 267,
                22: 258,
                3: 260,
                6: 259,
                12: 254,
                24: 270,
                19: 268,
                25: 255,
                13: 264,
                26: 259,
                27: 262,
                7: 262,
                14: 266,
                28: 257,
                23: 260,
                29: 253,
                15: 265
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "M61BURST": 0,
        "ALE39Loadout": 0,
        "UseLAU138": True,
        "INSAlignmentStored": False,
        "TacanChannel": 0,
        "TacanBand": 0,
        "IlsChannel": 1,
        "KY28Key": 1,
        "LGB1000": 1,
        "LGB100": 6,
        "LGB10": 8,
        "LGB1": 8,
    }

    class Properties:

        class M61BURST:
            id = "M61BURST"

            class Values:
                Burst_200 = 0
                Burst_100 = 1
                Burst_50 = 2
                Manual = 3

        class ALE39Loadout:
            id = "ALE39Loadout"

            class Values:
                _60_Flares___0_Chaff = 0
                _50_Flares___10_Chaff = 1
                _40_Flares___20_Chaff = 2
                _30_Flares___30_Chaff = 3
                _20_Flares___40_Chaff = 4
                _10_Flares___50_Chaff = 5
                _0_Flares___60_Chaff = 6

        class UseLAU138:
            id = "UseLAU138"

        class INSAlignmentStored:
            id = "INSAlignmentStored"

        class TacanChannel:
            id = "TacanChannel"

        class TacanBand:
            id = "TacanBand"

            class Values:
                X = 0
                Y = 1

        class IlsChannel:
            id = "IlsChannel"

        class KY28Key:
            id = "KY28Key"

        class LGB1000:
            id = "LGB1000"

        class LGB100:
            id = "LGB100"

        class LGB10:
            id = "LGB10"

        class LGB1:
            id = "LGB1"

    livery_name = "F-14B"  # from type

    class Pylon1:
        LAU_138_AIM_9M = (1, Weapons.LAU_138_AIM_9M)
        LAU_138_AIM_9L = (1, Weapons.LAU_138_AIM_9L)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod_ = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod_)
        CATM_9M = (1, Weapons.CATM_9M)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)

    class Pylon2:
        AIM_54C_Mk47_ = (2, Weapons.AIM_54C_Mk47_)
        AIM_54A_Mk47_ = (2, Weapons.AIM_54A_Mk47_)
        AIM_54A_Mk60_ = (2, Weapons.AIM_54A_Mk60_)
        AIM_7M = (2, Weapons.AIM_7M)
        AIM_7F = (2, Weapons.AIM_7F)
        AIM_7MH = (2, Weapons.AIM_7MH)
        LAU_7_AIM_9M = (2, Weapons.LAU_7_AIM_9M)
        LAU_7_AIM_9L = (2, Weapons.LAU_7_AIM_9L)
        LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_7P = (2, Weapons.AIM_7P)
        _2_LAU_10___4_ZUNI_MK_71_________ = (2, Weapons._2_LAU_10___4_ZUNI_MK_71_________)
        _2_Mk_81_____ = (2, Weapons._2_Mk_81_____)
        _2_Mk_82_______ = (2, Weapons._2_Mk_82_______)
        _2_Mk_82AIR_____ = (2, Weapons._2_Mk_82AIR_____)
        _2_Mk_82_SnakeEye_____ = (2, Weapons._2_Mk_82_SnakeEye_____)
        _2_MK_20_____ = (2, Weapons._2_MK_20_____)
        Mk_83______ = (2, Weapons.Mk_83______)
        _3_BDU_33____ = (2, Weapons._3_BDU_33____)
        _2_BDU_45_____ = (2, Weapons._2_BDU_45_____)
        _2_BDU_45B_____ = (2, Weapons._2_BDU_45B_____)

    class Pylon3:
        Fuel_tank_300_gal_ = (3, Weapons.Fuel_tank_300_gal_)
        Fuel_tank_300_gal__empty_ = (3, Weapons.Fuel_tank_300_gal__empty_)

    class Pylon4:
        AIM_54A_Mk47 = (4, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (4, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (4, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (4, Weapons.AIM_7M_)
        AIM_7F_ = (4, Weapons.AIM_7F_)
        AIM_7MH_ = (4, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (4, Weapons.AIM_7P_)
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (4, Weapons.Mk_82_SnakeEye)
        BDU_45 = (4, Weapons.BDU_45)
        BDU_45B = (4, Weapons.BDU_45B)
        MAK79_4_Mk_81 = (4, Weapons.MAK79_4_Mk_81)
        MAK79_4_Mk_82 = (4, Weapons.MAK79_4_Mk_82)
        MAK79_4_BDU_45 = (4, Weapons.MAK79_4_BDU_45)
        MAK79_4_BDU_45B = (4, Weapons.MAK79_4_BDU_45B)
        MAK79_4_BDU_33 = (4, Weapons.MAK79_4_BDU_33)
        _3_BDU_33_ = (4, Weapons._3_BDU_33_)
        MAK79_4_Mk_82AIR = (4, Weapons.MAK79_4_Mk_82AIR)
        MAK79_4_Mk_82_SnakeEye = (4, Weapons.MAK79_4_Mk_82_SnakeEye)
        MAK79_3_Mk_83 = (4, Weapons.MAK79_3_Mk_83)
        Mk_83 = (4, Weapons.Mk_83)
        GBU_12 = (4, Weapons.GBU_12)
        GBU_16 = (4, Weapons.GBU_16)
        _2_LAU_10___4_ZUNI_MK_71___ = (4, Weapons._2_LAU_10___4_ZUNI_MK_71___)
        Mk_20 = (4, Weapons.Mk_20)
        ADM_141A_ = (4, Weapons.ADM_141A_)
        Mk_84 = (4, Weapons.Mk_84)
        GBU_10 = (4, Weapons.GBU_10)
        MAK79_2_MK_20 = (4, Weapons.MAK79_2_MK_20)
        GBU_24 = (4, Weapons.GBU_24)

    class Pylon5:
        AIM_54A_Mk47 = (5, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (5, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (5, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (5, Weapons.AIM_7M_)
        AIM_7F_ = (5, Weapons.AIM_7F_)
        AIM_7MH_ = (5, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (5, Weapons.AIM_7P_)
        Mk_82 = (5, Weapons.Mk_82)
        Mk_82AIR = (5, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (5, Weapons.Mk_82_SnakeEye)
        BDU_45 = (5, Weapons.BDU_45)
        BDU_45B = (5, Weapons.BDU_45B)
        MAK79_3_Mk_81 = (5, Weapons.MAK79_3_Mk_81)
        MAK79_3_Mk_82 = (5, Weapons.MAK79_3_Mk_82)
        MAK79_3_BDU_45 = (5, Weapons.MAK79_3_BDU_45)
        MAK79_3_BDU_45B = (5, Weapons.MAK79_3_BDU_45B)
        MAK79_3_BDU_33 = (5, Weapons.MAK79_3_BDU_33)
        _3_BDU_33_ = (5, Weapons._3_BDU_33_)
        MAK79_3_Mk_82AIR = (5, Weapons.MAK79_3_Mk_82AIR)
        MAK79_3_Mk_82_SnakeEye = (5, Weapons.MAK79_3_Mk_82_SnakeEye)
        MAK79_Mk_83_ = (5, Weapons.MAK79_Mk_83_)
        Mk_83 = (5, Weapons.Mk_83)
        GBU_12 = (5, Weapons.GBU_12)
        GBU_16 = (5, Weapons.GBU_16)
        _2_SUU_25___8_LUU_2___ = (5, Weapons._2_SUU_25___8_LUU_2___)
        Mk_20 = (5, Weapons.Mk_20)
        ADM_141A_ = (5, Weapons.ADM_141A_)
        Mk_84 = (5, Weapons.Mk_84)
        MAK79_MK_20_ = (5, Weapons.MAK79_MK_20_)

    class Pylon6:
        AIM_54A_Mk47 = (6, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (6, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (6, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (6, Weapons.AIM_7M_)
        AIM_7F_ = (6, Weapons.AIM_7F_)
        AIM_7MH_ = (6, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (6, Weapons.AIM_7P_)
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82AIR = (6, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (6, Weapons.Mk_82_SnakeEye)
        BDU_45 = (6, Weapons.BDU_45)
        BDU_45B = (6, Weapons.BDU_45B)
        MAK79_3_Mk_81_ = (6, Weapons.MAK79_3_Mk_81_)
        MAK79_3_Mk_82_ = (6, Weapons.MAK79_3_Mk_82_)
        MAK79_3_BDU_45_ = (6, Weapons.MAK79_3_BDU_45_)
        MAK79_3_BDU_45B_ = (6, Weapons.MAK79_3_BDU_45B_)
        MAK79_3_BDU_33_ = (6, Weapons.MAK79_3_BDU_33_)
        _3_BDU_33_ = (6, Weapons._3_BDU_33_)
        MAK79_3_Mk_82AIR_ = (6, Weapons.MAK79_3_Mk_82AIR_)
        MAK79_3_Mk_82_SnakeEye_ = (6, Weapons.MAK79_3_Mk_82_SnakeEye_)
        MAK79_Mk_83 = (6, Weapons.MAK79_Mk_83)
        Mk_83 = (6, Weapons.Mk_83)
        GBU_12 = (6, Weapons.GBU_12)
        GBU_16 = (6, Weapons.GBU_16)
        SUU_25___8_LUU_2_ = (6, Weapons.SUU_25___8_LUU_2_)
        Mk_20 = (6, Weapons.Mk_20)
        ADM_141A_ = (6, Weapons.ADM_141A_)
        Mk_84 = (6, Weapons.Mk_84)
        MAK79_MK_20 = (6, Weapons.MAK79_MK_20)
        GBU_24 = (6, Weapons.GBU_24)

    class Pylon7:
        AIM_54A_Mk47 = (7, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (7, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (7, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (7, Weapons.AIM_7M_)
        AIM_7F_ = (7, Weapons.AIM_7F_)
        AIM_7MH_ = (7, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (7, Weapons.AIM_7P_)
        Mk_82 = (7, Weapons.Mk_82)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (7, Weapons.Mk_82_SnakeEye)
        BDU_45 = (7, Weapons.BDU_45)
        BDU_45B = (7, Weapons.BDU_45B)
        MAK79_4_Mk_81 = (7, Weapons.MAK79_4_Mk_81)
        MAK79_4_Mk_82 = (7, Weapons.MAK79_4_Mk_82)
        MAK79_4_BDU_45 = (7, Weapons.MAK79_4_BDU_45)
        MAK79_4_BDU_45B = (7, Weapons.MAK79_4_BDU_45B)
        MAK79_4_BDU_33 = (7, Weapons.MAK79_4_BDU_33)
        _3_BDU_33_ = (7, Weapons._3_BDU_33_)
        MAK79_4_Mk_82AIR = (7, Weapons.MAK79_4_Mk_82AIR)
        MAK79_4_Mk_82_SnakeEye = (7, Weapons.MAK79_4_Mk_82_SnakeEye)
        MAK79_3_Mk_83_ = (7, Weapons.MAK79_3_Mk_83_)
        Mk_83 = (7, Weapons.Mk_83)
        GBU_12 = (7, Weapons.GBU_12)
        GBU_16 = (7, Weapons.GBU_16)
        LAU_10___4_ZUNI_MK_71_ = (7, Weapons.LAU_10___4_ZUNI_MK_71_)
        Mk_20 = (7, Weapons.Mk_20)
        ADM_141A_ = (7, Weapons.ADM_141A_)
        Mk_84 = (7, Weapons.Mk_84)
        GBU_10 = (7, Weapons.GBU_10)
        MAK79_2_MK_20_ = (7, Weapons.MAK79_2_MK_20_)

    class Pylon8:
        Fuel_tank_300_gal_ = (8, Weapons.Fuel_tank_300_gal_)
        Fuel_tank_300_gal__empty_ = (8, Weapons.Fuel_tank_300_gal__empty_)

    class Pylon9:
        AIM_54C_Mk47__ = (9, Weapons.AIM_54C_Mk47__)
        AIM_54A_Mk47__ = (9, Weapons.AIM_54A_Mk47__)
        AIM_54A_Mk60__ = (9, Weapons.AIM_54A_Mk60__)
        AIM_7M = (9, Weapons.AIM_7M)
        AIM_7F = (9, Weapons.AIM_7F)
        AIM_7MH = (9, Weapons.AIM_7MH)
        LAU_7_AIM_9M = (9, Weapons.LAU_7_AIM_9M)
        LAU_7_AIM_9L = (9, Weapons.LAU_7_AIM_9L)
        LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_7P = (9, Weapons.AIM_7P)
        _2_LAU_10___4_ZUNI_MK_71______ = (9, Weapons._2_LAU_10___4_ZUNI_MK_71______)
        _2_Mk_81__ = (9, Weapons._2_Mk_81__)
        _2_Mk_82____ = (9, Weapons._2_Mk_82____)
        _2_Mk_82AIR__ = (9, Weapons._2_Mk_82AIR__)
        _2_Mk_82_SnakeEye__ = (9, Weapons._2_Mk_82_SnakeEye__)
        _2_MK_20__ = (9, Weapons._2_MK_20__)
        Mk_83___ = (9, Weapons.Mk_83___)
        _3_BDU_33____ = (9, Weapons._3_BDU_33____)
        _2_BDU_45__ = (9, Weapons._2_BDU_45__)
        _2_BDU_45B__ = (9, Weapons._2_BDU_45B__)
        LANTIRN_Targeting_Pod = (9, Weapons.LANTIRN_Targeting_Pod)

    class Pylon10:
        LAU_138_AIM_9M = (10, Weapons.LAU_138_AIM_9M)
        LAU_138_AIM_9L = (10, Weapons.LAU_138_AIM_9L)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod__ = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod__)
        CATM_9M = (10, Weapons.CATM_9M)
        Smokewinder___red = (10, Weapons.Smokewinder___red)
        Smokewinder___green = (10, Weapons.Smokewinder___green)
        Smokewinder___blue = (10, Weapons.Smokewinder___blue)
        Smokewinder___white = (10, Weapons.Smokewinder___white)
        Smokewinder___yellow = (10, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (10, Weapons.Smokewinder___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.AntishipStrike, task.CAS]
    task_default = task.Intercept


class F_14A_135_GR(PlaneType):
    id = "F-14A-135-GR"
    flyable = True
    height = 4.8
    width = 10.15
    length = 16.6
    fuel_max = 7348
    max_speed = 2520
    chaff = 140
    flare = 60
    charge_total = 200
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                20: 269,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                19: 268,
                15: 265
            },
        },
        2: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                20: 269,
                30: 263,
                21: 225,
                11: 267,
                22: 258,
                3: 260,
                6: 259,
                12: 254,
                24: 270,
                19: 268,
                25: 255,
                13: 264,
                26: 259,
                27: 262,
                7: 262,
                14: 266,
                28: 257,
                23: 260,
                29: 253,
                15: 265
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "M61BURST": 0,
        "ALE39Loadout": 0,
        "UseLAU138": True,
        "INSAlignmentStored": False,
        "TacanChannel": 0,
        "TacanBand": 0,
        "IlsChannel": 1,
        "KY28Key": 1,
        "LGB1000": 1,
        "LGB100": 6,
        "LGB10": 8,
        "LGB1": 8,
    }

    class Properties:

        class M61BURST:
            id = "M61BURST"

            class Values:
                Burst_200 = 0
                Burst_100 = 1
                Burst_50 = 2
                Manual = 3

        class ALE39Loadout:
            id = "ALE39Loadout"

            class Values:
                _60_Flares___0_Chaff = 0
                _50_Flares___10_Chaff = 1
                _40_Flares___20_Chaff = 2
                _30_Flares___30_Chaff = 3
                _20_Flares___40_Chaff = 4
                _10_Flares___50_Chaff = 5
                _0_Flares___60_Chaff = 6

        class UseLAU138:
            id = "UseLAU138"

        class INSAlignmentStored:
            id = "INSAlignmentStored"

        class TacanChannel:
            id = "TacanChannel"

        class TacanBand:
            id = "TacanBand"

            class Values:
                X = 0
                Y = 1

        class IlsChannel:
            id = "IlsChannel"

        class KY28Key:
            id = "KY28Key"

        class LGB1000:
            id = "LGB1000"

        class LGB100:
            id = "LGB100"

        class LGB10:
            id = "LGB10"

        class LGB1:
            id = "LGB1"

    livery_name = "F-14A-135-GR"  # from type

    class Pylon1:
        LAU_138_AIM_9M = (1, Weapons.LAU_138_AIM_9M)
        LAU_138_AIM_9L = (1, Weapons.LAU_138_AIM_9L)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod_ = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod_)
        CATM_9M = (1, Weapons.CATM_9M)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)

    class Pylon2:
        AIM_54C_Mk47_ = (2, Weapons.AIM_54C_Mk47_)
        AIM_54A_Mk47_ = (2, Weapons.AIM_54A_Mk47_)
        AIM_54A_Mk60_ = (2, Weapons.AIM_54A_Mk60_)
        AIM_7M = (2, Weapons.AIM_7M)
        AIM_7F = (2, Weapons.AIM_7F)
        AIM_7MH = (2, Weapons.AIM_7MH)
        LAU_7_AIM_9M = (2, Weapons.LAU_7_AIM_9M)
        LAU_7_AIM_9L = (2, Weapons.LAU_7_AIM_9L)
        LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_7P = (2, Weapons.AIM_7P)
        _2_LAU_10___4_ZUNI_MK_71_________ = (2, Weapons._2_LAU_10___4_ZUNI_MK_71_________)
        _2_Mk_81_____ = (2, Weapons._2_Mk_81_____)
        _2_Mk_82_______ = (2, Weapons._2_Mk_82_______)
        _2_Mk_82AIR_____ = (2, Weapons._2_Mk_82AIR_____)
        _2_Mk_82_SnakeEye_____ = (2, Weapons._2_Mk_82_SnakeEye_____)
        _2_MK_20_____ = (2, Weapons._2_MK_20_____)
        Mk_83______ = (2, Weapons.Mk_83______)
        _3_BDU_33____ = (2, Weapons._3_BDU_33____)
        _2_BDU_45_____ = (2, Weapons._2_BDU_45_____)
        _2_BDU_45B_____ = (2, Weapons._2_BDU_45B_____)

    class Pylon3:
        Fuel_tank_300_gal_ = (3, Weapons.Fuel_tank_300_gal_)
        Fuel_tank_300_gal__empty_ = (3, Weapons.Fuel_tank_300_gal__empty_)

    class Pylon4:
        AIM_54A_Mk47 = (4, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (4, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (4, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (4, Weapons.AIM_7M_)
        AIM_7F_ = (4, Weapons.AIM_7F_)
        AIM_7MH_ = (4, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (4, Weapons.AIM_7P_)
        Mk_82 = (4, Weapons.Mk_82)
        Mk_82AIR = (4, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (4, Weapons.Mk_82_SnakeEye)
        BDU_45 = (4, Weapons.BDU_45)
        BDU_45B = (4, Weapons.BDU_45B)
        MAK79_4_Mk_81 = (4, Weapons.MAK79_4_Mk_81)
        MAK79_4_Mk_82 = (4, Weapons.MAK79_4_Mk_82)
        MAK79_4_BDU_45 = (4, Weapons.MAK79_4_BDU_45)
        MAK79_4_BDU_45B = (4, Weapons.MAK79_4_BDU_45B)
        MAK79_4_BDU_33 = (4, Weapons.MAK79_4_BDU_33)
        _3_BDU_33_ = (4, Weapons._3_BDU_33_)
        MAK79_4_Mk_82AIR = (4, Weapons.MAK79_4_Mk_82AIR)
        MAK79_4_Mk_82_SnakeEye = (4, Weapons.MAK79_4_Mk_82_SnakeEye)
        MAK79_3_Mk_83 = (4, Weapons.MAK79_3_Mk_83)
        Mk_83 = (4, Weapons.Mk_83)
        GBU_12 = (4, Weapons.GBU_12)
        GBU_16 = (4, Weapons.GBU_16)
        _2_LAU_10___4_ZUNI_MK_71___ = (4, Weapons._2_LAU_10___4_ZUNI_MK_71___)
        Mk_20 = (4, Weapons.Mk_20)
        ADM_141A_ = (4, Weapons.ADM_141A_)
        Mk_84 = (4, Weapons.Mk_84)
        GBU_10 = (4, Weapons.GBU_10)
        MAK79_2_MK_20 = (4, Weapons.MAK79_2_MK_20)
        GBU_24 = (4, Weapons.GBU_24)

    class Pylon5:
        AIM_54A_Mk47 = (5, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (5, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (5, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (5, Weapons.AIM_7M_)
        AIM_7F_ = (5, Weapons.AIM_7F_)
        AIM_7MH_ = (5, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (5, Weapons.AIM_7P_)
        Mk_82 = (5, Weapons.Mk_82)
        Mk_82AIR = (5, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (5, Weapons.Mk_82_SnakeEye)
        BDU_45 = (5, Weapons.BDU_45)
        BDU_45B = (5, Weapons.BDU_45B)
        MAK79_3_Mk_81 = (5, Weapons.MAK79_3_Mk_81)
        MAK79_3_Mk_82 = (5, Weapons.MAK79_3_Mk_82)
        MAK79_3_BDU_45 = (5, Weapons.MAK79_3_BDU_45)
        MAK79_3_BDU_45B = (5, Weapons.MAK79_3_BDU_45B)
        MAK79_3_BDU_33 = (5, Weapons.MAK79_3_BDU_33)
        _3_BDU_33_ = (5, Weapons._3_BDU_33_)
        MAK79_3_Mk_82AIR = (5, Weapons.MAK79_3_Mk_82AIR)
        MAK79_3_Mk_82_SnakeEye = (5, Weapons.MAK79_3_Mk_82_SnakeEye)
        MAK79_Mk_83_ = (5, Weapons.MAK79_Mk_83_)
        Mk_83 = (5, Weapons.Mk_83)
        GBU_12 = (5, Weapons.GBU_12)
        GBU_16 = (5, Weapons.GBU_16)
        _2_SUU_25___8_LUU_2___ = (5, Weapons._2_SUU_25___8_LUU_2___)
        Mk_20 = (5, Weapons.Mk_20)
        ADM_141A_ = (5, Weapons.ADM_141A_)
        Mk_84 = (5, Weapons.Mk_84)
        MAK79_MK_20_ = (5, Weapons.MAK79_MK_20_)

    class Pylon6:
        AIM_54A_Mk47 = (6, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (6, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (6, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (6, Weapons.AIM_7M_)
        AIM_7F_ = (6, Weapons.AIM_7F_)
        AIM_7MH_ = (6, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (6, Weapons.AIM_7P_)
        Mk_82 = (6, Weapons.Mk_82)
        Mk_82AIR = (6, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (6, Weapons.Mk_82_SnakeEye)
        BDU_45 = (6, Weapons.BDU_45)
        BDU_45B = (6, Weapons.BDU_45B)
        MAK79_3_Mk_81_ = (6, Weapons.MAK79_3_Mk_81_)
        MAK79_3_Mk_82_ = (6, Weapons.MAK79_3_Mk_82_)
        MAK79_3_BDU_45_ = (6, Weapons.MAK79_3_BDU_45_)
        MAK79_3_BDU_45B_ = (6, Weapons.MAK79_3_BDU_45B_)
        MAK79_3_BDU_33_ = (6, Weapons.MAK79_3_BDU_33_)
        _3_BDU_33_ = (6, Weapons._3_BDU_33_)
        MAK79_3_Mk_82AIR_ = (6, Weapons.MAK79_3_Mk_82AIR_)
        MAK79_3_Mk_82_SnakeEye_ = (6, Weapons.MAK79_3_Mk_82_SnakeEye_)
        MAK79_Mk_83 = (6, Weapons.MAK79_Mk_83)
        Mk_83 = (6, Weapons.Mk_83)
        GBU_12 = (6, Weapons.GBU_12)
        GBU_16 = (6, Weapons.GBU_16)
        SUU_25___8_LUU_2_ = (6, Weapons.SUU_25___8_LUU_2_)
        Mk_20 = (6, Weapons.Mk_20)
        ADM_141A_ = (6, Weapons.ADM_141A_)
        Mk_84 = (6, Weapons.Mk_84)
        MAK79_MK_20 = (6, Weapons.MAK79_MK_20)
        GBU_24 = (6, Weapons.GBU_24)

    class Pylon7:
        AIM_54A_Mk47 = (7, Weapons.AIM_54A_Mk47)
        AIM_54A_Mk60 = (7, Weapons.AIM_54A_Mk60)
        AIM_54C_Mk47 = (7, Weapons.AIM_54C_Mk47)
        AIM_7M_ = (7, Weapons.AIM_7M_)
        AIM_7F_ = (7, Weapons.AIM_7F_)
        AIM_7MH_ = (7, Weapons.AIM_7MH_)
#ERRR <CLEAN>
        AIM_7P_ = (7, Weapons.AIM_7P_)
        Mk_82 = (7, Weapons.Mk_82)
        Mk_82AIR = (7, Weapons.Mk_82AIR)
        Mk_82_SnakeEye = (7, Weapons.Mk_82_SnakeEye)
        BDU_45 = (7, Weapons.BDU_45)
        BDU_45B = (7, Weapons.BDU_45B)
        MAK79_4_Mk_81 = (7, Weapons.MAK79_4_Mk_81)
        MAK79_4_Mk_82 = (7, Weapons.MAK79_4_Mk_82)
        MAK79_4_BDU_45 = (7, Weapons.MAK79_4_BDU_45)
        MAK79_4_BDU_45B = (7, Weapons.MAK79_4_BDU_45B)
        MAK79_4_BDU_33 = (7, Weapons.MAK79_4_BDU_33)
        _3_BDU_33_ = (7, Weapons._3_BDU_33_)
        MAK79_4_Mk_82AIR = (7, Weapons.MAK79_4_Mk_82AIR)
        MAK79_4_Mk_82_SnakeEye = (7, Weapons.MAK79_4_Mk_82_SnakeEye)
        MAK79_3_Mk_83_ = (7, Weapons.MAK79_3_Mk_83_)
        Mk_83 = (7, Weapons.Mk_83)
        GBU_12 = (7, Weapons.GBU_12)
        GBU_16 = (7, Weapons.GBU_16)
        LAU_10___4_ZUNI_MK_71_ = (7, Weapons.LAU_10___4_ZUNI_MK_71_)
        Mk_20 = (7, Weapons.Mk_20)
        ADM_141A_ = (7, Weapons.ADM_141A_)
        Mk_84 = (7, Weapons.Mk_84)
        GBU_10 = (7, Weapons.GBU_10)
        MAK79_2_MK_20_ = (7, Weapons.MAK79_2_MK_20_)

    class Pylon8:
        Fuel_tank_300_gal_ = (8, Weapons.Fuel_tank_300_gal_)
        Fuel_tank_300_gal__empty_ = (8, Weapons.Fuel_tank_300_gal__empty_)

    class Pylon9:
        AIM_54C_Mk47__ = (9, Weapons.AIM_54C_Mk47__)
        AIM_54A_Mk47__ = (9, Weapons.AIM_54A_Mk47__)
        AIM_54A_Mk60__ = (9, Weapons.AIM_54A_Mk60__)
        AIM_7M = (9, Weapons.AIM_7M)
        AIM_7F = (9, Weapons.AIM_7F)
        AIM_7MH = (9, Weapons.AIM_7MH)
        LAU_7_AIM_9M = (9, Weapons.LAU_7_AIM_9M)
        LAU_7_AIM_9L = (9, Weapons.LAU_7_AIM_9L)
        LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_7P = (9, Weapons.AIM_7P)
        _2_LAU_10___4_ZUNI_MK_71______ = (9, Weapons._2_LAU_10___4_ZUNI_MK_71______)
        _2_Mk_81__ = (9, Weapons._2_Mk_81__)
        _2_Mk_82____ = (9, Weapons._2_Mk_82____)
        _2_Mk_82AIR__ = (9, Weapons._2_Mk_82AIR__)
        _2_Mk_82_SnakeEye__ = (9, Weapons._2_Mk_82_SnakeEye__)
        _2_MK_20__ = (9, Weapons._2_MK_20__)
        Mk_83___ = (9, Weapons.Mk_83___)
        _3_BDU_33____ = (9, Weapons._3_BDU_33____)
        _2_BDU_45__ = (9, Weapons._2_BDU_45__)
        _2_BDU_45B__ = (9, Weapons._2_BDU_45B__)
        LANTIRN_Targeting_Pod = (9, Weapons.LANTIRN_Targeting_Pod)

    class Pylon10:
        LAU_138_AIM_9M = (10, Weapons.LAU_138_AIM_9M)
        LAU_138_AIM_9L = (10, Weapons.LAU_138_AIM_9L)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod__ = (10, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod__)
        CATM_9M = (10, Weapons.CATM_9M)
        Smokewinder___red = (10, Weapons.Smokewinder___red)
        Smokewinder___green = (10, Weapons.Smokewinder___green)
        Smokewinder___blue = (10, Weapons.Smokewinder___blue)
        Smokewinder___white = (10, Weapons.Smokewinder___white)
        Smokewinder___yellow = (10, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (10, Weapons.Smokewinder___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.AntishipStrike, task.CAS]
    task_default = task.Intercept


class FA_18C_hornet(PlaneType):
    id = "FA-18C_hornet"
    flyable = True
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 4900
    max_speed = 1950.12
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
        2: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Hornet",
            "Squid",
            "Ragin",
            "Roman",
            "Sting",
            "Jury",
            "Joker",
            "Ram",
            "Hawk",
            "Devil",
            "Check",
            "Snake",
        ]
    }

    property_defaults: Dict[str, Any] = {
        "OuterBoard": 0,
        "InnerBoard": 0,
        "HelmetMountedDevice": 1,
    }

    class Properties:

        class OuterBoard:
            id = "OuterBoard"

            class Values:
                Single = 0
                Ripple = 1

        class InnerBoard:
            id = "InnerBoard"

            class Values:
                Single = 0
                Ripple = 1

        class HelmetMountedDevice:
            id = "HelmetMountedDevice"

            class Values:
                Not_installed = 0
                JHMCS = 1
                NVG = 2

    livery_name = "FA-18C_HORNET"  # from type

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (1, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        LAU_115_2_LAU_127_AIM_9M = (2, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (2, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (2, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (2, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (2, Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (2, Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar = (2, Weapons.LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar)
        LAU_115_2_LAU_127_AIM_120B = (2, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (2, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (2, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (2, Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BDU_45___500lb_Practice_Bomb = (2, Weapons.BDU_45___500lb_Practice_Bomb)
        BDU_45B___500lb_Practice_Bomb = (2, Weapons.BDU_45B___500lb_Practice_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (2, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (2, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (2, Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (2, Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD)
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD)
        BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb = (2, Weapons.BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb)
        BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb = (2, Weapons.BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb)
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb)
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (2, Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (2, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (2, Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD)
        AGM_154A___JSOW_CEB__CBU_type_ = (2, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (2, Weapons.BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (2, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (2, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb = (2, Weapons.GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (2, Weapons.GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (2, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_ = (2, Weapons.AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_)
        BDU_45_LG___500lb_Practice_Laser_Guided_Bomb = (2, Weapons.BDU_45_LG___500lb_Practice_Laser_Guided_Bomb)
        BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb = (2, Weapons.BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb)
        AGM_84D_Harpoon_AShM = (2, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (2, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_84H_SLAM_ER__Expanded_Response_ = (2, Weapons.AGM_84H_SLAM_ER__Expanded_Response_)
        AWW_13_DATALINK_POD = (2, Weapons.AWW_13_DATALINK_POD)
        BRU_42_with_3_x_ADM_141A_TALD = (2, Weapons.BRU_42_with_3_x_ADM_141A_TALD)
        BRU_42_with_2_x_ADM_141A_TALD = (2, Weapons.BRU_42_with_2_x_ADM_141A_TALD)
        BRU_42_with_ADM_141A_TALD = (2, Weapons.BRU_42_with_ADM_141A_TALD)
#ERRR <CLEAN>
        LAU_115_LAU_127_AIM_9X = (2, Weapons.LAU_115_LAU_127_AIM_9X)
        LAU_115_LAU_127_AIM_9L = (2, Weapons.LAU_115_LAU_127_AIM_9L)
        LAU_115_LAU_127_AIM_9M = (2, Weapons.LAU_115_LAU_127_AIM_9M)
        LAU_115_LAU_127_CATM_9M = (2, Weapons.LAU_115_LAU_127_CATM_9M)
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (2, Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM)
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (2, Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM)

    class Pylon3:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (3, Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (3, Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar = (3, Weapons.LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar)
        LAU_115_2_LAU_127_AIM_120B = (3, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (3, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (3, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (3, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (3, Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BDU_45___500lb_Practice_Bomb = (3, Weapons.BDU_45___500lb_Practice_Bomb)
        BDU_45B___500lb_Practice_Bomb = (3, Weapons.BDU_45B___500lb_Practice_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (3, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (3, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (3, Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (3, Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD)
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD)
        BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb = (3, Weapons.BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb)
        BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb = (3, Weapons.BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb)
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb)
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (3, Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (3, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (3, Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (3, Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (3, Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD)
        AGM_154A___JSOW_CEB__CBU_type_ = (3, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (3, Weapons.BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (3, Weapons.GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (3, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BDU_45_LG___500lb_Practice_Laser_Guided_Bomb = (3, Weapons.BDU_45_LG___500lb_Practice_Laser_Guided_Bomb)
        BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb = (3, Weapons.BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb)
        AGM_84D_Harpoon_AShM = (3, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_84H_SLAM_ER__Expanded_Response_ = (3, Weapons.AGM_84H_SLAM_ER__Expanded_Response_)
        AWW_13_DATALINK_POD = (3, Weapons.AWW_13_DATALINK_POD)
        FPU_8A_Fuel_Tank_330_gallons = (3, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        BRU_42_with_3_x_ADM_141A_TALD = (3, Weapons.BRU_42_with_3_x_ADM_141A_TALD)
        BRU_42_with_2_x_ADM_141A_TALD = (3, Weapons.BRU_42_with_2_x_ADM_141A_TALD)
        BRU_42_with_ADM_141A_TALD = (3, Weapons.BRU_42_with_ADM_141A_TALD)
#ERRR <CLEAN>
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (3, Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM)
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (3, Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM)

    class Pylon4:
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7P_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7P_Sparrow_Semi_Active_Radar)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AN_AAQ_28_LITENING___Targeting_Pod_ = (4, Weapons.AN_AAQ_28_LITENING___Targeting_Pod_)
        AN_ASQ_228_ATFLIR___Targeting_Pod = (4, Weapons.AN_ASQ_228_ATFLIR___Targeting_Pod)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (5, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (5, Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BDU_45___500lb_Practice_Bomb = (5, Weapons.BDU_45___500lb_Practice_Bomb)
        BDU_45B___500lb_Practice_Bomb = (5, Weapons.BDU_45B___500lb_Practice_Bomb)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (5, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (5, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (5, Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (5, Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (5, Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD)
        BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb = (5, Weapons.BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb)
        BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb = (5, Weapons.BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb)
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (5, Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (5, Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        AN_AAQ_28_LITENING___Targeting_Pod = (5, Weapons.AN_AAQ_28_LITENING___Targeting_Pod)
        AWW_13_DATALINK_POD = (5, Weapons.AWW_13_DATALINK_POD)
        FPU_8A_Fuel_Tank_330_gallons = (5, Weapons.FPU_8A_Fuel_Tank_330_gallons)
#ERRR <CLEAN>

    class Pylon6:
        AIM_7M_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7MH_Sparrow_Semi_Active_Radar)
        AIM_7P_Sparrow_Semi_Active_Radar = (6, Weapons.AIM_7P_Sparrow_Semi_Active_Radar)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (6, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (6, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)

    class Pylon7:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (7, Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (7, Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar = (7, Weapons.LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar)
        LAU_115_2_LAU_127_AIM_120B = (7, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (7, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (7, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (7, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (7, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (7, Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD)
        Mk_83___1000lb_GP_Bomb_LD = (7, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BDU_45___500lb_Practice_Bomb = (7, Weapons.BDU_45___500lb_Practice_Bomb)
        BDU_45B___500lb_Practice_Bomb = (7, Weapons.BDU_45B___500lb_Practice_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (7, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (7, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (7, Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (7, Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD)
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (7, Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD)
        BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb = (7, Weapons.BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb)
        BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb = (7, Weapons.BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb)
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb)
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (7, Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (7, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (7, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (7, Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (7, Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (7, Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (7, Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD)
        AGM_154A___JSOW_CEB__CBU_type_ = (7, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154C___JSOW_Unitary_BROACH = (7, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (7, Weapons.BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH = (7, Weapons.BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb = (7, Weapons.GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (7, Weapons.GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (7, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb = (7, Weapons.GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (7, Weapons.BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BDU_45_LG___500lb_Practice_Laser_Guided_Bomb = (7, Weapons.BDU_45_LG___500lb_Practice_Laser_Guided_Bomb)
        BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb = (7, Weapons.BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb)
        AGM_84D_Harpoon_AShM = (7, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (7, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_84H_SLAM_ER__Expanded_Response_ = (7, Weapons.AGM_84H_SLAM_ER__Expanded_Response_)
        AWW_13_DATALINK_POD = (7, Weapons.AWW_13_DATALINK_POD)
        FPU_8A_Fuel_Tank_330_gallons = (7, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        BRU_42_with_3_x_ADM_141A_TALD = (7, Weapons.BRU_42_with_3_x_ADM_141A_TALD)
        BRU_42_with_2_x_ADM_141A_TALD = (7, Weapons.BRU_42_with_2_x_ADM_141A_TALD)
        BRU_42_with_ADM_141A_TALD = (7, Weapons.BRU_42_with_ADM_141A_TALD)
#ERRR <CLEAN>
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM_ = (7, Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM_)
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM_ = (7, Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM_)

    class Pylon8:
        LAU_115_2_LAU_127_AIM_9M = (8, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (8, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (8, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (8, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (8, Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (8, Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar)
        LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar = (8, Weapons.LAU_115C_with_AIM_7P_Sparrow_Semi_Active_Radar)
        LAU_115_2_LAU_127_AIM_120B = (8, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (8, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (8, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (8, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (8, Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD)
        Mk_83___1000lb_GP_Bomb_LD = (8, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BDU_45___500lb_Practice_Bomb = (8, Weapons.BDU_45___500lb_Practice_Bomb)
        BDU_45B___500lb_Practice_Bomb = (8, Weapons.BDU_45B___500lb_Practice_Bomb)
        GBU_10___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (8, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        CBU_99___490lbs__247_x_HEAT_Bomblets = (8, Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (8, Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (8, Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD)
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (8, Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD)
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (8, Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD)
        BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb = (8, Weapons.BRU_33_with_2_x_BDU_45___500lb_Practice_Bomb)
        BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb = (8, Weapons.BRU_33_with_2_x_BDU_45B___500lb_Practice_Bomb)
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb)
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (8, Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets)
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (8, Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT)
        BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (8, Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD)
        AGM_154A___JSOW_CEB__CBU_type_ = (8, Weapons.AGM_154A___JSOW_CEB__CBU_type_)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_ = (8, Weapons.BRU_55_with_2_x_AGM_154A___JSOW_CEB__CBU_type_)
        BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.BRU_55_with_2_x_AGM_154C___JSOW_Unitary_BROACH)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_2_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (8, Weapons.GBU_31_V_4_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb)
        GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb = (8, Weapons.GBU_32_V_2_B___JDAM__1000lb_GPS_Guided_Bomb)
        GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_24A_B_Paveway_III___2000lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.BRU_55_with_2_x_GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_ = (8, Weapons.AGM_62_Walleye_II___Guided_Weapon_Mk_5__TV_Guided_)
        BDU_45_LG___500lb_Practice_Laser_Guided_Bomb = (8, Weapons.BDU_45_LG___500lb_Practice_Laser_Guided_Bomb)
        BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb = (8, Weapons.BRU_33_with_2_x_BDU_45_LG_500lb_Practice_Laser_Guided_Bomb)
        AGM_84D_Harpoon_AShM = (8, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (8, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_84H_SLAM_ER__Expanded_Response_ = (8, Weapons.AGM_84H_SLAM_ER__Expanded_Response_)
        AWW_13_DATALINK_POD = (8, Weapons.AWW_13_DATALINK_POD)
        BRU_42_with_3_x_ADM_141A_TALD = (8, Weapons.BRU_42_with_3_x_ADM_141A_TALD)
        BRU_42_with_2_x_ADM_141A_TALD = (8, Weapons.BRU_42_with_2_x_ADM_141A_TALD)
        BRU_42_with_ADM_141A_TALD = (8, Weapons.BRU_42_with_ADM_141A_TALD)
#ERRR <CLEAN>
        LAU_115_LAU_127_AIM_9X_R = (8, Weapons.LAU_115_LAU_127_AIM_9X_R)
        LAU_115_LAU_127_AIM_9L_R = (8, Weapons.LAU_115_LAU_127_AIM_9L_R)
        LAU_115_LAU_127_AIM_9M_R = (8, Weapons.LAU_115_LAU_127_AIM_9M_R)
        LAU_115_LAU_127_CATM_9M_R = (8, Weapons.LAU_115_LAU_127_CATM_9M_R)
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM_ = (8, Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM_)
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM_ = (8, Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM_)

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (9, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (9, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon10:
        Smoke_Generator___red_ = (10, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (10, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (10, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (10, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (10, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (10, Weapons.Smoke_Generator___orange_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.PinpointStrike, task.CAS, task.GroundAttack, task.RunwayAttack, task.SEAD, task.AFAC, task.AntishipStrike, task.Reconnaissance]
    task_default = task.CAP


class Hawk(PlaneType):
    id = "Hawk"
    flyable = True
    height = 4.02
    width = 9.418
    length = 11.98
    fuel_max = 1272
    max_speed = 2880
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265
            },
        },
    }

    livery_name = "HAWK"  # from type

    class Pylon1:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (1, Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM)

    class Pylon2:
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BRU_42_3_BDU_33 = (2, Weapons.BRU_42_3_BDU_33)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon3:
        ADEN_GUNPOD = (3, Weapons.ADEN_GUNPOD)

    class Pylon4:
        Matra_Type_155_Rocket_Pod = (4, Weapons.Matra_Type_155_Rocket_Pod)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon5:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (5, Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM)

    class Pylon6:
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept]
    task_default = task.CAP


class I_16(PlaneType):
    id = "I-16"
    height = 3.25
    width = 9.004
    length = 6.13
    fuel_max = 191
    max_speed = 464.4
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "landingTorch": False,
    }

    class Properties:

        class landingTorch:
            id = "landingTorch"

    livery_name = "I-16"  # from type

    class Pylon1:
        I16_RS_82 = (1, Weapons.I16_RS_82)

    class Pylon2:
        I16_RS_82 = (2, Weapons.I16_RS_82)

    class Pylon3:
        I16_RS_82 = (3, Weapons.I16_RS_82)

    class Pylon4:
        I16_FAB_100SV = (4, Weapons.I16_FAB_100SV)
        I16_DROP_FUEL_TANK = (4, Weapons.I16_DROP_FUEL_TANK)

    class Pylon5:
        I16_FAB_100SV = (5, Weapons.I16_FAB_100SV)
        I16_DROP_FUEL_TANK = (5, Weapons.I16_DROP_FUEL_TANK)

    class Pylon6:
        I16_RS_82 = (6, Weapons.I16_RS_82)

    class Pylon7:
        I16_RS_82 = (7, Weapons.I16_RS_82)

    class Pylon8:
        I16_RS_82 = (8, Weapons.I16_RS_82)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept, task.Reconnaissance]
    task_default = task.CAP


class L_39C(PlaneType):
    id = "L-39C"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 980
    max_speed = 763.2
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": 1,
        "NS430allow": True,
        "DismountIFRHood": False,
        "DismountGunSight": False,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class NS430allow:
            id = "NS430allow"

        class DismountIFRHood:
            id = "DismountIFRHood"

        class DismountGunSight:
            id = "DismountGunSight"

    livery_name = "L-39C"  # from type

    class Pylon1:
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (1, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        P_50T___50kg_Practice_Bomb_LD = (1, Weapons.P_50T___50kg_Practice_Bomb_LD)
        Fuel_Tank_150_liters = (1, Weapons.Fuel_Tank_150_liters)
        R_3S___AAM__IR_guided = (1, Weapons.R_3S___AAM__IR_guided)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        Smoke_Generator___red_ = (2, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (2, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (2, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (2, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (2, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (2, Weapons.Smoke_Generator___orange_)

    class Pylon3:
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        P_50T___50kg_Practice_Bomb_LD = (3, Weapons.P_50T___50kg_Practice_Bomb_LD)
        Fuel_Tank_150_liters = (3, Weapons.Fuel_Tank_150_liters)
        R_3S___AAM__IR_guided = (3, Weapons.R_3S___AAM__IR_guided)
        Smoke_Generator___red = (3, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (3, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (3, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (3, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (3, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (3, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.CAS, task.AFAC, task.CAP, task.AntishipStrike]
    task_default = task.CAS


class L_39ZA(PlaneType):
    id = "L-39ZA"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 980
    max_speed = 763.2
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 0
    flare_charge_size = 0
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": 1,
        "NS430allow": True,
        "DismountIFRHood": False,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class NS430allow:
            id = "NS430allow"

        class DismountIFRHood:
            id = "DismountIFRHood"

    livery_name = "L-39ZA"  # from livery_entry

    class Pylon1:
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        OFAB_100_Jupiter___100kg_GP_Bomb_HD = (1, Weapons.OFAB_100_Jupiter___100kg_GP_Bomb_HD)
        P_50T___50kg_Practice_Bomb_LD = (1, Weapons.P_50T___50kg_Practice_Bomb_LD)
        _2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD = (1, Weapons._2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (1, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        PK_3___7_62mm_GPMG = (1, Weapons.PK_3___7_62mm_GPMG)
        R_3S___AAM__IR_guided = (1, Weapons.R_3S___AAM__IR_guided)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (1, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        OFAB_100_Jupiter___100kg_GP_Bomb_HD = (2, Weapons.OFAB_100_Jupiter___100kg_GP_Bomb_HD)
        P_50T___50kg_Practice_Bomb_LD = (2, Weapons.P_50T___50kg_Practice_Bomb_LD)
        _2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD = (2, Weapons._2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        PK_3___7_62mm_GPMG = (2, Weapons.PK_3___7_62mm_GPMG)
        Fuel_Tank_150_liters = (2, Weapons.Fuel_Tank_150_liters)
        Fuel_Tank_350_liters = (2, Weapons.Fuel_Tank_350_liters)

    class Pylon3:
        Smoke_Generator___red_ = (3, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (3, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (3, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (3, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (3, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (3, Weapons.Smoke_Generator___orange_)

    class Pylon4:
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        OFAB_100_Jupiter___100kg_GP_Bomb_HD = (4, Weapons.OFAB_100_Jupiter___100kg_GP_Bomb_HD)
        P_50T___50kg_Practice_Bomb_LD = (4, Weapons.P_50T___50kg_Practice_Bomb_LD)
        _2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD = (4, Weapons._2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (4, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        PK_3___7_62mm_GPMG = (4, Weapons.PK_3___7_62mm_GPMG)
        Fuel_Tank_150_liters = (4, Weapons.Fuel_Tank_150_liters)
        Fuel_Tank_350_liters = (4, Weapons.Fuel_Tank_350_liters)

    class Pylon5:
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        OFAB_100_Jupiter___100kg_GP_Bomb_HD = (5, Weapons.OFAB_100_Jupiter___100kg_GP_Bomb_HD)
        P_50T___50kg_Practice_Bomb_LD = (5, Weapons.P_50T___50kg_Practice_Bomb_LD)
        _2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD = (5, Weapons._2_x_OFAB_100_Jupiter___100kg_GP_Bombs_HD)
        UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_16UM_pod___16_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        PK_3___7_62mm_GPMG = (5, Weapons.PK_3___7_62mm_GPMG)
        R_3S___AAM__IR_guided = (5, Weapons.R_3S___AAM__IR_guided)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        Smoke_Generator___red = (5, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (5, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (5, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (5, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (5, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (5, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5}

    tasks = [task.GroundAttack, task.RunwayAttack, task.CAS, task.AFAC, task.CAP, task.AntishipStrike]
    task_default = task.CAS


class M_2000C(PlaneType):
    id = "M-2000C"
    flyable = True
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3165
    max_speed = 2376
    chaff = 234
    flare = 64
    charge_total = 3024
    chaff_charge_size = 8
    flare_charge_size = 18
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    panel_radio = {
        1: {
            "channels": {
                1: 305,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 252,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
        2: {
            "channels": {
                1: 129,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 139,
                13: 140,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "RocketBurst": 6,
        "GunBurst": 1,
        "LaserCode100": 6,
        "LaserCode10": 8,
        "LaserCode1": 8,
        "WpBullseye": 0,
        "ForceINSRules": False,
        "ReadyALCM": True,
        "LoadNVGCase": False,
        "InitHotDrift": 0,
        "EnableTAF": True,
        "DisableVTBExport": False,
    }

    class Properties:

        class RocketBurst:
            id = "RocketBurst"

            class Values:
                _1_Rocket = 1
                _3_Rockets = 3
                _6_Rockets = 6
                _18_Rockets = 18

        class GunBurst:
            id = "GunBurst"

            class Values:
                _0_5_Second = 1
                _1_0_Second = 2

        class LaserCode100:
            id = "LaserCode100"

        class LaserCode10:
            id = "LaserCode10"

        class LaserCode1:
            id = "LaserCode1"

        class WpBullseye:
            id = "WpBullseye"

        class ForceINSRules:
            id = "ForceINSRules"

        class ReadyALCM:
            id = "ReadyALCM"

        class LoadNVGCase:
            id = "LoadNVGCase"

        class InitHotDrift:
            id = "InitHotDrift"

        class EnableTAF:
            id = "EnableTAF"

        class DisableVTBExport:
            id = "DisableVTBExport"

    livery_name = "M-2000C"  # from type

    class Pylon1:
        Matra_Magic_II = (1, Weapons.Matra_Magic_II)
        Matra_Magic_II___DDM = (1, Weapons.Matra_Magic_II___DDM)
        Matra_Type_155_Rocket_Pod = (1, Weapons.Matra_Type_155_Rocket_Pod)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)

    class Pylon2:
        Matra_Magic_II = (2, Weapons.Matra_Magic_II)
        Matra_Super_530D = (2, Weapons.Matra_Super_530D)
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (2, Weapons.BLG_66_AC_Belouga)
        SAMP_250___250_kg_GP_Bomb_LD = (2, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (2, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)
        AUF2_MK_82_x_2 = (2, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (2, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_MK_82_Air_x_2 = (2, Weapons.AUF2_MK_82_Air_x_2)
        AUF2_BLG_66_AC_x_2 = (2, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_SAMP_250_x_2 = (2, Weapons.AUF2_SAMP_250_x_2)
        AUF2_SAMP_250_HD_x_2 = (2, Weapons.AUF2_SAMP_250_HD_x_2)
        RPL_541_2000_liters_Fuel_Tank_ = (2, Weapons.RPL_541_2000_liters_Fuel_Tank_)
        RPL_541_2000_liters_Fuel_Tank__Empty_ = (2, Weapons.RPL_541_2000_liters_Fuel_Tank__Empty_)

    class Pylon3:
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (3, Weapons.BLG_66_AC_Belouga)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        SAMP_250___250_kg_GP_Bomb_LD = (3, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (3, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)

    class Pylon4:
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (4, Weapons.BLG_66_AC_Belouga)
        SAMP_250___250_kg_GP_Bomb_LD = (4, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (4, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)

    class Pylon5:
        BLG_66_AC_Belouga = (5, Weapons.BLG_66_AC_Belouga)
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (5, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (5, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        BAP_100_x_6 = (5, Weapons.BAP_100_x_6)
        BAP_100_x_12 = (5, Weapons.BAP_100_x_12)
        BAP_100_x_18 = (5, Weapons.BAP_100_x_18)
        AUF2_GBU_12_x_2 = (5, Weapons.AUF2_GBU_12_x_2)
        RPL_522_1300_liters_Fuel_Tank = (5, Weapons.RPL_522_1300_liters_Fuel_Tank)
        RPL_522_1300_liters_Fuel_Tank__Empty_ = (5, Weapons.RPL_522_1300_liters_Fuel_Tank__Empty_)
        Smokewinder___red = (5, Weapons.Smokewinder___red)
        Smokewinder___green = (5, Weapons.Smokewinder___green)
        Smokewinder___blue = (5, Weapons.Smokewinder___blue)
        Smokewinder___white = (5, Weapons.Smokewinder___white)
        Smokewinder___yellow = (5, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (5, Weapons.Smokewinder___orange)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (6, Weapons.BLG_66_AC_Belouga)
        SAMP_250___250_kg_GP_Bomb_LD = (6, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (6, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (7, Weapons.BLG_66_AC_Belouga)
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        SAMP_250___250_kg_GP_Bomb_LD = (7, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (7, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)

    class Pylon8:
        Matra_Magic_II = (8, Weapons.Matra_Magic_II)
        Matra_Super_530D = (8, Weapons.Matra_Super_530D)
        Matra_Type_155_Rocket_Pod = (8, Weapons.Matra_Type_155_Rocket_Pod)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (8, Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD)
        BLG_66_AC_Belouga = (8, Weapons.BLG_66_AC_Belouga)
        SAMP_250___250_kg_GP_Bomb_LD = (8, Weapons.SAMP_250___250_kg_GP_Bomb_LD)
        SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD = (8, Weapons.SAMP_250___250_kg_GP_Chute_Retarded_Bomb_HD)
        AUF2_MK_82_x_2 = (8, Weapons.AUF2_MK_82_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (8, Weapons.AUF2_MK_82_Snakeyes_x_2)
        AUF2_MK_82_Air_x_2 = (8, Weapons.AUF2_MK_82_Air_x_2)
        AUF2_BLG_66_AC_x_2 = (8, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_SAMP_250_x_2 = (8, Weapons.AUF2_SAMP_250_x_2)
        AUF2_SAMP_250_HD_x_2 = (8, Weapons.AUF2_SAMP_250_HD_x_2)
        RPL_541_2000_liters_Fuel_Tank__ = (8, Weapons.RPL_541_2000_liters_Fuel_Tank__)
        RPL_541_2000_liters_Fuel_Tank__Empty__ = (8, Weapons.RPL_541_2000_liters_Fuel_Tank__Empty__)

    class Pylon9:
        Matra_Magic_II = (9, Weapons.Matra_Magic_II)
        Matra_Magic_II___DDM = (9, Weapons.Matra_Magic_II___DDM)
        Matra_Type_155_Rocket_Pod = (9, Weapons.Matra_Type_155_Rocket_Pod)
        Smokewinder___red = (9, Weapons.Smokewinder___red)
        Smokewinder___green = (9, Weapons.Smokewinder___green)
        Smokewinder___blue = (9, Weapons.Smokewinder___blue)
        Smokewinder___white = (9, Weapons.Smokewinder___white)
        Smokewinder___yellow = (9, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (9, Weapons.Smokewinder___orange)

    class Pylon10:
        Eclair_16_flares_16_chaffs = (10, Weapons.Eclair_16_flares_16_chaffs)
        Eclair_M_0_6__108_chaffs = (10, Weapons.Eclair_M_0_6__108_chaffs)
        Eclair_M_1_5__8_flares_90_chaffs = (10, Weapons.Eclair_M_1_5__8_flares_90_chaffs)
        Eclair_M_2_4__16_flares_72_chaffs = (10, Weapons.Eclair_M_2_4__16_flares_72_chaffs)
        Eclair_M_3_3__24_flares_54_chaffs = (10, Weapons.Eclair_M_3_3__24_flares_54_chaffs)
        Eclair_M_4_2__32_flares_36_chaffs = (10, Weapons.Eclair_M_4_2__32_flares_36_chaffs)
        Eclair_M_5_1__40_flares_18_chaffs = (10, Weapons.Eclair_M_5_1__40_flares_18_chaffs)
        Eclair_M_6_0__48_flares = (10, Weapons.Eclair_M_6_0__48_flares)

    class Pylon11:
        A_G_Training = (11, Weapons.A_G_Training)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS, task.AFAC, task.CAP, task.Escort, task.FighterSweep, task.Intercept]
    task_default = task.CAP


class MQ_9_Reaper(PlaneType):
    id = "MQ-9 Reaper"
    group_size_max = 1
    height = 4.77
    width = 20
    length = 11
    fuel_max = 1300
    max_speed = 400
    eplrs = True

    livery_name = "MQ-9 REAPER"  # from type

    class Pylon1:
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (1, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM114x2_OH_58 = (1, Weapons.AGM114x2_OH_58)
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)

    class Pylon2:
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM114x2_OH_58 = (2, Weapons.AGM114x2_OH_58)

    class Pylon3:
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM114x2_OH_58 = (3, Weapons.AGM114x2_OH_58)

    class Pylon4:
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM114x2_OH_58 = (4, Weapons.AGM114x2_OH_58)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.GroundAttack, task.CAS, task.AFAC, task.Reconnaissance]
    task_default = task.Reconnaissance


class MiG_15bis(PlaneType):
    id = "MiG-15bis"
    flyable = True
    height = 3.7
    width = 10.08
    length = 10.11
    fuel_max = 1172
    max_speed = 992
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 3.75

    livery_name = "MIG-15BIS"  # from livery_entry

    class Pylon1:
        FAB_50 = (1, Weapons.FAB_50)
        FAB_100M = (1, Weapons.FAB_100M)
        PTB400_MIG15 = (1, Weapons.PTB400_MIG15)
        PTB600_MIG15 = (1, Weapons.PTB600_MIG15)
        PTB300_MIG15 = (1, Weapons.PTB300_MIG15)

    class Pylon2:
        FAB_50 = (2, Weapons.FAB_50)
        FAB_100M = (2, Weapons.FAB_100M)
        PTB400_MIG15 = (2, Weapons.PTB400_MIG15)
        PTB600_MIG15 = (2, Weapons.PTB600_MIG15)
        PTB300_MIG15 = (2, Weapons.PTB300_MIG15)

    pylons: Set[int] = {1, 2}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept]
    task_default = task.CAP


class MiG_19P(PlaneType):
    id = "MiG-19P"
    flyable = True
    height = 3.8885
    width = 9
    length = 13.025
    fuel_max = 1800
    max_speed = 992
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 135,
                2: 124,
                3: 122,
                1: 121,
                4: 125,
                5: 127
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "MountSIRENA": False,
        "MissileToneVolume": 5,
        "NAV_Initial_Hdg": 0,
        "ADF_FAR_Frequency": 625,
        "ADF_NEAR_Frequency": 303,
        "ADF_Selected_Frequency": 1,
    }

    class Properties:

        class MountSIRENA:
            id = "MountSIRENA"

        class MissileToneVolume:
            id = "MissileToneVolume"

        class NAV_Initial_Hdg:
            id = "NAV_Initial_Hdg"

        class ADF_FAR_Frequency:
            id = "ADF_FAR_Frequency"

        class ADF_NEAR_Frequency:
            id = "ADF_NEAR_Frequency"

        class ADF_Selected_Frequency:
            id = "ADF_Selected_Frequency"

            class Values:
                FAR = 1
                NEAR = 2

    livery_name = "MIG-19P"  # from type

    class Pylon1:
        K_13A = (1, Weapons.K_13A)
        Smoke_Generator___red = (1, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (1, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (1, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (1, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (1, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (1, Weapons.Smoke_Generator___orange)

    class Pylon2:
        FAB_50 = (2, Weapons.FAB_50)
        FAB_100M = (2, Weapons.FAB_100M)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        ORO_57K___S_5M_x_8 = (2, Weapons.ORO_57K___S_5M_x_8)
        PTB760_MIG19 = (2, Weapons.PTB760_MIG19)

    class Pylon3:
        ORO_57K___S_5M_x_8 = (3, Weapons.ORO_57K___S_5M_x_8)

    class Pylon4:
        ORO_57K___S_5M_x_8 = (4, Weapons.ORO_57K___S_5M_x_8)

    class Pylon5:
        FAB_50 = (5, Weapons.FAB_50)
        FAB_100M = (5, Weapons.FAB_100M)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        ORO_57K___S_5M_x_8 = (5, Weapons.ORO_57K___S_5M_x_8)
        PTB760_MIG19 = (5, Weapons.PTB760_MIG19)

    class Pylon6:
        K_13A = (6, Weapons.K_13A)
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___green = (6, Weapons.Smoke_Generator___green)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___yellow = (6, Weapons.Smoke_Generator___yellow)
        Smoke_Generator___orange = (6, Weapons.Smoke_Generator___orange)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAP, task.CAS, task.Escort, task.FighterSweep, task.GroundAttack, task.Intercept]
    task_default = task.CAP


class MiG_21Bis(PlaneType):
    id = "MiG-21Bis"
    flyable = True
    height = 4.125
    width = 7.154
    length = 14.5
    fuel_max = 2280
    max_speed = 2509.2
    chaff = 18
    flare = 40
    charge_total = 58
    chaff_charge_size = 1
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 124,
                2: 150,
                4: 131,
                8: 133,
                16: 123,
                17: 132,
                9: 122,
                18: 127,
                5: 141,
                10: 124,
                20: 138,
                11: 134,
                3: 121,
                6: 126,
                12: 125,
                13: 135,
                7: 130,
                14: 137,
                19: 129,
                15: 136
            },
        },
    }

    livery_name = "MIG-21BIS"  # from livery_entry

    class Pylon1:
        UB_16UM___16_S_5M = (1, Weapons.UB_16UM___16_S_5M)
        S_24B__21____180_kg__fragmented_unguided_rocket = (1, Weapons.S_24B__21____180_kg__fragmented_unguided_rocket)
        S_24A__21____180_kg__cumulative_unguided_rocket = (1, Weapons.S_24A__21____180_kg__cumulative_unguided_rocket)
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (1, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_250_M54_TU___235_kg__bomb__parachute = (1, Weapons.FAB_250_M54_TU___235_kg__bomb__parachute)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        R_13M___AAM__IR_guided = (1, Weapons.R_13M___AAM__IR_guided)
        R_13M1___AAM__IR_guided = (1, Weapons.R_13M1___AAM__IR_guided)
        R_3R___AAM__radar_guided = (1, Weapons.R_3R___AAM__radar_guided)
        R_3S___AAM__IR_guided = (1, Weapons.R_3S___AAM__IR_guided)
        RS2US___AAM__beam_rider = (1, Weapons.RS2US___AAM__beam_rider)
        R_60 = (1, Weapons.R_60)
        R_60M = (1, Weapons.R_60M)
        R_60M_x_2 = (1, Weapons.R_60M_x_2)
        R_60_x_2 = (1, Weapons.R_60_x_2)
        Fuel_Tank_490_L__21_ = (1, Weapons.Fuel_Tank_490_L__21_)

    class Pylon2:
        UB_16UM___16_S_5M = (2, Weapons.UB_16UM___16_S_5M)
        UB_32M___32_S_5M = (2, Weapons.UB_32M___32_S_5M)
        S_24B__21____180_kg__fragmented_unguided_rocket = (2, Weapons.S_24B__21____180_kg__fragmented_unguided_rocket)
        S_24A__21____180_kg__cumulative_unguided_rocket = (2, Weapons.S_24A__21____180_kg__cumulative_unguided_rocket)
        FAB_100_x_4 = (2, Weapons.FAB_100_x_4)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (2, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (2, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Kh_66_Grom__21____AGM__radar_guided_APU_68 = (2, Weapons.Kh_66_Grom__21____AGM__radar_guided_APU_68)
        R_13M___AAM__IR_guided = (2, Weapons.R_13M___AAM__IR_guided)
        R_13M1___AAM__IR_guided = (2, Weapons.R_13M1___AAM__IR_guided)
        R_3R___AAM__radar_guided = (2, Weapons.R_3R___AAM__radar_guided)
        R_3S___AAM__IR_guided = (2, Weapons.R_3S___AAM__IR_guided)
        RS2US___AAM__beam_rider = (2, Weapons.RS2US___AAM__beam_rider)
        R_55___AAM__IR_guided = (2, Weapons.R_55___AAM__IR_guided)
        R_60 = (2, Weapons.R_60)
        R_60M = (2, Weapons.R_60M)
        R_60M_x_2 = (2, Weapons.R_60M_x_2)
        R_60_x_2 = (2, Weapons.R_60_x_2)
        UPK_23_250___gun_pod = (2, Weapons.UPK_23_250___gun_pod)

    class Pylon3:
        RN_24___470kg__nuclear_bomb__free_fall = (3, Weapons.RN_24___470kg__nuclear_bomb__free_fall)
        RN_28___260_kg__nuclear_bomb__free_fall = (3, Weapons.RN_28___260_kg__nuclear_bomb__free_fall)
        SPS_141_100__21____jamming_and_countermeasures_pod = (3, Weapons.SPS_141_100__21____jamming_and_countermeasures_pod)
        Fuel_Tank_490_L_Central__21_ = (3, Weapons.Fuel_Tank_490_L_Central__21_)
        Fuel_Tank_800_L__21_ = (3, Weapons.Fuel_Tank_800_L__21_)

    class Pylon4:
        UB_16UM___16_S_5M = (4, Weapons.UB_16UM___16_S_5M)
        UB_32M___32_S_5M = (4, Weapons.UB_32M___32_S_5M)
        S_24B__21____180_kg__fragmented_unguided_rocket = (4, Weapons.S_24B__21____180_kg__fragmented_unguided_rocket)
        S_24A__21____180_kg__cumulative_unguided_rocket = (4, Weapons.S_24A__21____180_kg__cumulative_unguided_rocket)
        FAB_100_x_4 = (4, Weapons.FAB_100_x_4)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        BL_755_CBU___450kg__147_Frag_Pen_bomblets = (4, Weapons.BL_755_CBU___450kg__147_Frag_Pen_bomblets)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        Kh_66_Grom__21____AGM__radar_guided_APU_68 = (4, Weapons.Kh_66_Grom__21____AGM__radar_guided_APU_68)
        R_13M___AAM__IR_guided = (4, Weapons.R_13M___AAM__IR_guided)
        R_13M1___AAM__IR_guided = (4, Weapons.R_13M1___AAM__IR_guided)
        R_3R___AAM__radar_guided = (4, Weapons.R_3R___AAM__radar_guided)
        R_3S___AAM__IR_guided = (4, Weapons.R_3S___AAM__IR_guided)
        RS2US___AAM__beam_rider = (4, Weapons.RS2US___AAM__beam_rider)
        R_55___AAM__IR_guided = (4, Weapons.R_55___AAM__IR_guided)
        R_60 = (4, Weapons.R_60)
        R_60M = (4, Weapons.R_60M)
        R_60M_x_2_ = (4, Weapons.R_60M_x_2_)
        R_60_x_2_ = (4, Weapons.R_60_x_2_)
        UPK_23_250___gun_pod = (4, Weapons.UPK_23_250___gun_pod)

    class Pylon5:
        UB_16UM___16_S_5M = (5, Weapons.UB_16UM___16_S_5M)
        S_24B__21____180_kg__fragmented_unguided_rocket = (5, Weapons.S_24B__21____180_kg__fragmented_unguided_rocket)
        S_24A__21____180_kg__cumulative_unguided_rocket = (5, Weapons.S_24A__21____180_kg__cumulative_unguided_rocket)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        FAB_250_M54_TU___235_kg__bomb__parachute = (5, Weapons.FAB_250_M54_TU___235_kg__bomb__parachute)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        R_13M___AAM__IR_guided = (5, Weapons.R_13M___AAM__IR_guided)
        R_13M1___AAM__IR_guided = (5, Weapons.R_13M1___AAM__IR_guided)
        R_3R___AAM__radar_guided = (5, Weapons.R_3R___AAM__radar_guided)
        R_3S___AAM__IR_guided = (5, Weapons.R_3S___AAM__IR_guided)
        RS2US___AAM__beam_rider = (5, Weapons.RS2US___AAM__beam_rider)
        R_60 = (5, Weapons.R_60)
        R_60M = (5, Weapons.R_60M)
        R_60M_x_2_ = (5, Weapons.R_60M_x_2_)
        R_60_x_2_ = (5, Weapons.R_60_x_2_)
        Fuel_Tank_490_L__21_ = (5, Weapons.Fuel_Tank_490_L__21_)

    class Pylon6:
        ASO_2___countermeasures_pod = (6, Weapons.ASO_2___countermeasures_pod)
        SPRD_99_takeoff_rocket = (6, Weapons.SPRD_99_takeoff_rocket)

    class Pylon7:
        Smoke___white___21_ = (7, Weapons.Smoke___white___21_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.Intercept, task.CAP, task.Escort, task.CAS, task.GroundAttack]
    task_default = task.CAP


class Su_34(PlaneType):
    id = "Su-34"
    height = 6
    width = 14.7
    length = 23.3
    fuel_max = 9800
    max_speed = 1900.008
    chaff = 64
    flare = 64
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    livery_name = "SU-34"  # from type

    class Pylon1:
        R_73__AA_11_Archer____Infra_Red = (1, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)
        L175V_Khibiny_ECM_pod = (1, Weapons.L175V_Khibiny_ECM_pod)

    class Pylon2:
        R_73__AA_11_Archer____Infra_Red = (2, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (2, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon3:
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (3, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (3, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (3, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (3, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (3, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (3, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (3, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (3, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (3, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (3, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        R_73__AA_11_Archer____Infra_Red = (3, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (3, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (3, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (3, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (3, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (3, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (3, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon4:
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (4, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (4, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (4, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (4, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (4, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (4, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (4, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (4, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (4, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (4, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (4, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (4, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (4, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        R_77__AA_12_Adder____Active_Rdr = (4, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (4, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (4, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (4, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (4, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (4, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (4, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (4, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (4, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (4, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (4, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)

    class Pylon5:
        R_77__AA_12_Adder____Active_Rdr = (5, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (5, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (5, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (5, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (5, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (5, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (5, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (5, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (5, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (5, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (5, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (5, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (5, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (5, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (5, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (5, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)

    class Pylon6:
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (6, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (6, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (6, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (6, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (6, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (6, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (6, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (6, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (6, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (6, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)

    class Pylon7:
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (7, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (7, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (7, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (7, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (7, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (7, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (7, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (7, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (7, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (7, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (7, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (7, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (7, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (7, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (7, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (7, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (7, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (7, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (7, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (7, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD = (7, Weapons.MBD3_U6_68_with_6_x_FAB_250___250kg_GP_Bombs_LD)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (7, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)

    class Pylon8:
        R_77__AA_12_Adder____Active_Rdr = (8, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (8, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (8, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (8, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (8, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (8, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (8, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (8, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (8, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (8, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (8, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (8, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (8, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (8, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (8, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (8, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (8, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (8, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (8, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (8, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (8, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (8, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (8, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (8, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (8, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)

    class Pylon9:
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (9, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (9, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (9, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (9, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (9, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (9, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (9, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (9, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (9, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (9, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (9, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (9, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (9, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (9, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (9, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (9, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (9, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (9, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (9, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (9, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (9, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (9, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (9, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (9, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (9, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (9, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (9, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (9, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        R_77__AA_12_Adder____Active_Rdr = (9, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (9, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (9, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (9, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (9, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        FAB_1500_M_54___1500kg_GP_Bomb_LD = (9, Weapons.FAB_1500_M_54___1500kg_GP_Bomb_LD)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (9, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (9, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb = (9, Weapons.KAB_1500LG_Pr___1500kg_Laser_Guided_Penetrator_Bomb)
        KAB_1500Kr___1500kg_TV_Guided_Bomb = (9, Weapons.KAB_1500Kr___1500kg_TV_Guided_Bomb)
        Kh_59M__AS_18_Kazoo____930kg__ASM__IN = (9, Weapons.Kh_59M__AS_18_Kazoo____930kg__ASM__IN)

    class Pylon10:
        Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__ = (10, Weapons.Kh_29T__AS_14_Kedge____670kg__ASM__TV_Guided__)
        Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__ = (10, Weapons.Kh_29L__AS_14_Kedge____657kg__ASM__Semi_Act_Laser__)
        Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__ = (10, Weapons.Kh_31A__AS_17_Krypton____610kg__AShM__IN__Act_Rdr__)
        Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__ = (10, Weapons.Kh_31P__AS_17_Krypton____600kg__ARM__IN__Pas_Rdr__)
        Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr = (10, Weapons.Kh_35__AS_20_Kayak____520kg__AShM__IN__Act_Rdr)
        Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_ = (10, Weapons.Kh_58U__AS_11_Kilter____640kg__ARM__IN__Pas_Rdr_)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (10, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (10, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (10, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_25_O___420mm_UnGd_Rkt__380kg_Frag = (10, Weapons.S_25_O___420mm_UnGd_Rkt__380kg_Frag)
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (10, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (10, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (10, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (10, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (10, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (10, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (10, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (10, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (10, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (10, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        KAB_500LG___500kg_Laser_Guided_Bomb = (10, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (10, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        KAB_500S___500kg_GPS_Guided_Bomb = (10, Weapons.KAB_500S___500kg_GPS_Guided_Bomb)
        SAB_100___100kg_flare_illumination_Bomb = (10, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_100___100kg_GP_Bomb_LD = (10, Weapons.FAB_100___100kg_GP_Bomb_LD)
        MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD = (10, Weapons.MBD3_U6_68_with_6_x_FAB_100___100kg_GP_Bombs_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (10, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (10, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        R_73__AA_11_Archer____Infra_Red = (10, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (10, Weapons.R_77__AA_12_Adder____Active_Rdr)
        R_27R__AA_10_Alamo_A____Semi_Act_Rdr = (10, Weapons.R_27R__AA_10_Alamo_A____Semi_Act_Rdr)
        R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range = (10, Weapons.R_27ER__AA_10_Alamo_C____Semi_Act_Extended_Range)
        R_27T__AA_10_Alamo_B____Infra_Red = (10, Weapons.R_27T__AA_10_Alamo_B____Infra_Red)
        R_27ET__AA_10_Alamo_D____IR_Extended_Range = (10, Weapons.R_27ET__AA_10_Alamo_D____IR_Extended_Range)
        MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD = (10, Weapons.MBD3_U6_68_with_5_x_FAB_250___250kg_GP_Bombs_LD)

    class Pylon11:
        R_73__AA_11_Archer____Infra_Red = (11, Weapons.R_73__AA_11_Archer____Infra_Red)
        R_77__AA_12_Adder____Active_Rdr = (11, Weapons.R_77__AA_12_Adder____Active_Rdr)

    class Pylon12:
        R_73__AA_11_Archer____Infra_Red = (12, Weapons.R_73__AA_11_Archer____Infra_Red)
        L005_Sorbtsiya_ECM_pod__right_ = (12, Weapons.L005_Sorbtsiya_ECM_pod__right_)
        L175V_Khibiny_ECM_pod = (12, Weapons.L175V_Khibiny_ECM_pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    tasks = [task.AFAC, task.SEAD, task.AntishipStrike, task.CAS, task.PinpointStrike, task.GroundAttack, task.RunwayAttack]
    task_default = task.GroundAttack


class Yak_52(PlaneType):
    id = "Yak-52"
    flyable = True
    height = 2.7
    width = 9.3
    length = 7.745
    fuel_max = 87.84
    max_speed = 270
    radio_frequency = 132

    panel_radio = {
        1: {
            "channels": {
                6: 0.803,
                2: 0.303,
                8: 0.215,
                3: 0.289,
                1: 0.625,
                4: 0.591,
                5: 0.408,
                7: 0.443
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "PropellorType": 0,
        "NetCrewControlPriority": 0,
    }

    class Properties:

        class SoloFlight:
            id = "SoloFlight"

        class PropellorType:
            id = "PropellorType"

            class Values:
                _2_Blade_V530TA_D35 = 0
                _3_Blade_MTV_9 = 1

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

    livery_name = "YAK-52"  # from type

    class Pylon1:
        Smoke_Generator___red_ = (1, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (1, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (1, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (1, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (1, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (1, Weapons.Smoke_Generator___orange_)

    pylons: Set[int] = {1}

    tasks = [task.CAP, task.Escort, task.AFAC]
    task_default = task.AFAC


class B_17G(PlaneType):
    id = "B-17G"
    height = 5.82
    width = 31.62
    length = 22.66
    fuel_max = 7600
    max_speed = 522

    callnames: Dict[str, List[str]] = {
        "USA": [
        ]
    }

    property_defaults: Dict[str, Any] = {
    }


    class Pylon1:
        _12_AN_M64___500lb_GP_Bomb_LD = (1, Weapons._12_AN_M64___500lb_GP_Bomb_LD)

    pylons: Set[int] = {1}

    tasks = [task.GroundAttack, task.RunwayAttack]
    task_default = task.GroundAttack


class Ju_88A4(PlaneType):
    id = "Ju-88A4"
    height = 5.07
    width = 20.08
    length = 14.35
    fuel_max = 2120
    max_speed = 540

    callnames: Dict[str, List[str]] = {
        "USA": [
        ]
    }

    property_defaults: Dict[str, Any] = {
    }


    class Pylon1:
        LTF_5b_Aerial_Torpedo = (1, Weapons.LTF_5b_Aerial_Torpedo)
        SC_250_Type_1_L2___250kg_GP_Bomb_LD = (1, Weapons.SC_250_Type_1_L2___250kg_GP_Bomb_LD)
        SC_501_SC250 = (1, Weapons.SC_501_SC250)
        SC_501_SC500 = (1, Weapons.SC_501_SC500)
        SC_500_L2___500kg_GP_Bomb_LD = (1, Weapons.SC_500_L2___500kg_GP_Bomb_LD)
        SD_250_Stg___250kg_GP_Bomb_LD = (1, Weapons.SD_250_Stg___250kg_GP_Bomb_LD)
        SD_500_A___500kg_GP_Bomb_LD = (1, Weapons.SD_500_A___500kg_GP_Bomb_LD)
        AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions = (1, Weapons.AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions)
        AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions = (1, Weapons.AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions)
        AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions = (1, Weapons.AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions)

    class Pylon3:
        LTF_5b_Aerial_Torpedo = (3, Weapons.LTF_5b_Aerial_Torpedo)
        SC_250_Type_1_L2___250kg_GP_Bomb_LD = (3, Weapons.SC_250_Type_1_L2___250kg_GP_Bomb_LD)
        SC_501_SC250 = (3, Weapons.SC_501_SC250)
        SC_501_SC500 = (3, Weapons.SC_501_SC500)
        SC_500_L2___500kg_GP_Bomb_LD = (3, Weapons.SC_500_L2___500kg_GP_Bomb_LD)
        SD_250_Stg___250kg_GP_Bomb_LD = (3, Weapons.SD_250_Stg___250kg_GP_Bomb_LD)
        SD_500_A___500kg_GP_Bomb_LD = (3, Weapons.SD_500_A___500kg_GP_Bomb_LD)
        AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions = (3, Weapons.AB_250_2___144_x_SD_2__250kg_CBU_with_HE_submunitions)
        AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions = (3, Weapons.AB_250_2___17_x_SD_10A__250kg_CBU_with_10kg_Frag_HE_submunitions)
        AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions = (3, Weapons.AB_500_1___34_x_SD_10A__500kg_CBU_with_10kg_Frag_HE_submunitions)

    pylons: Set[int] = {1, 3}

    tasks = [task.GroundAttack, task.RunwayAttack, task.AntishipStrike, task.CAS]
    task_default = task.GroundAttack


class C_47(PlaneType):
    id = "C-47"
    height = 5.16
    width = 29.11
    length = 19.43
    fuel_max = 1470
    max_speed = 369

    callnames: Dict[str, List[str]] = {
        "USA": [
        ]
    }

    property_defaults: Dict[str, Any] = {
    }


    pylons: Set[int] = set()

    tasks = [task.Transport, task.Escort, task.AFAC]
    task_default = task.Transport


class TF_51D(PlaneType):
    id = "TF-51D"
    flyable = True
    height = 4.77
    width = 9.12
    length = 12.13
    fuel_max = 501
    max_speed = 763.2
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                1: 105,
                2: 124,
                4: 139,
                3: 131
            },
        },
        2: {
            "channels": {
                1: 108.9
            },
        },
    }

    livery_name = "TF-51D"  # from type

    pylons: Set[int] = set()

    tasks = [task.Reconnaissance]
    task_default = task.Reconnaissance


plane_map = {
    "Tornado GR4": Tornado_GR4,
    "Tornado IDS": Tornado_IDS,
    "F/A-18A": F_A_18A,
    "F/A-18C": F_A_18C,
    "F-14A": F_14A,
    "Tu-22M3": Tu_22M3,
    "F-4E": F_4E,
    "B-52H": B_52H,
    "MiG-27K": MiG_27K,
    "Su-27": Su_27,
    "MiG-23MLD": MiG_23MLD,
    "Su-25": Su_25,
    "Su-25TM": Su_25TM,
    "Su-25T": Su_25T,
    "Su-33": Su_33,
    "MiG-25PD": MiG_25PD,
    "MiG-25RBT": MiG_25RBT,
    "Su-30": Su_30,
    "Su-17M4": Su_17M4,
    "MiG-31": MiG_31,
    "Tu-95MS": Tu_95MS,
    "Su-24M": Su_24M,
    "Su-24MR": Su_24MR,
    "Tu-160": Tu_160,
    "F-117A": F_117A,
    "B-1B": B_1B,
    "S-3B": S_3B,
    "S-3B Tanker": S_3B_Tanker,
    "Mirage 2000-5": Mirage_2000_5,
    "F-15C": F_15C,
    "F-15E": F_15E,
    "MiG-29A": MiG_29A,
    "MiG-29G": MiG_29G,
    "MiG-29S": MiG_29S,
    "Tu-142": Tu_142,
    "C-130": C_130,
    "An-26B": An_26B,
    "An-30M": An_30M,
    "C-17A": C_17A,
    "A-50": A_50,
    "E-3A": E_3A,
    "IL-78M": IL_78M,
    "E-2C": E_2C,
    "IL-76MD": IL_76MD,
    "F-16C bl.50": F_16C_bl_50,
    "F-16C bl.52d": F_16C_bl_52d,
    "F-16A": F_16A,
    "F-16A MLU": F_16A_MLU,
    "RQ-1A Predator": RQ_1A_Predator,
    "Yak-40": Yak_40,
    "KC-135": KC_135,
    "FW-190D9": FW_190D9,
    "FW-190A8": FW_190A8,
    "Bf-109K-4": Bf_109K_4,
    "SpitfireLFMkIX": SpitfireLFMkIX,
    "SpitfireLFMkIXCW": SpitfireLFMkIXCW,
    "P-51D": P_51D,
    "P-51D-30-NA": P_51D_30_NA,
    "P-47D-30": P_47D_30,
    "P-47D-30bl1": P_47D_30bl1,
    "P-47D-40": P_47D_40,
    "MosquitoFBMkVI": MosquitoFBMkVI,
    "A-20G": A_20G,
    "A-10A": A_10A,
    "A-10C": A_10C,
    "A-10C_2": A_10C_2,
    "AJS37": AJS37,
    "AV8BNA": AV8BNA,
    "KC130": KC130,
    "KC135MPRS": KC135MPRS,
    "C-101EB": C_101EB,
    "C-101CC": C_101CC,
    "J-11A": J_11A,
    "JF-17": JF_17,
    "KJ-2000": KJ_2000,
    "WingLoong-I": WingLoong_I,
    "H-6J": H_6J,
    "Christen Eagle II": Christen_Eagle_II,
    "F-16C_50": F_16C_50,
    "F-5E": F_5E,
    "F-5E-3": F_5E_3,
    "F-86F Sabre": F_86F_Sabre,
    "F-14B": F_14B,
    "F-14A-135-GR": F_14A_135_GR,
    "FA-18C_hornet": FA_18C_hornet,
    "Hawk": Hawk,
    "I-16": I_16,
    "L-39C": L_39C,
    "L-39ZA": L_39ZA,
    "M-2000C": M_2000C,
    "MQ-9 Reaper": MQ_9_Reaper,
    "MiG-15bis": MiG_15bis,
    "MiG-19P": MiG_19P,
    "MiG-21Bis": MiG_21Bis,
    "Su-34": Su_34,
    "Yak-52": Yak_52,
    "B-17G": B_17G,
    "Ju-88A4": Ju_88A4,
    "C-47": C_47,
    "TF-51D": TF_51D,
}
