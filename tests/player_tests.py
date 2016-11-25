from nose.tools import *
from CHAOS.player import *

def test_gets():
    # Name only
    # Check if all the attributions are correct
    p1 = Player("Avestruz")
    assert_equal(p1.name, "Avestruz")
    assert_equal(p1.maxEnergy, 0)
    assert_equal(p1.maxSkill, 0)
    assert_equal(p1.maxMagic, 0)
    assert_equal(p1.maxLuck, 0)
    assert_equal(p1.energy, 0)
    assert_equal(p1.skill, 0)
    assert_equal(p1.magic, 0)
    assert_equal(p1.luck, 0)
    assert_equal(p1.gold, 0)
    assert_equal(p1.backpack, [])
    assert_equal(p1.scroll, [])
    assert_equal(p1.armor, None)
    assert_equal(p1.weapon, None)
    assert_equal(p1.offhand, None)

    # Check if all gets are working
    assert_equal(p1.getName(), "Avestruz")
    assert_equal(p1.getMaxEnergy(), 0)
    assert_equal(p1.getMaxSkill(), 0)
    assert_equal(p1.getMaxMagic(), 0)
    assert_equal(p1.getMaxLuck(), 0)
    assert_equal(p1.getEnergy(), 0)
    assert_equal(p1.getSkill(), 0)
    assert_equal(p1.getMagic(), 0)
    assert_equal(p1.getLuck(), 0)
    assert_equal(p1.getGold(), 0)
    assert_equal(p1.getBackpack(), [])
    assert_equal(p1.getScroll(), [])
    assert_equal(p1.getArmor(), None)
    assert_equal(p1.getWeapon(), None)
    assert_equal(p1.getOffhand(), None)

    # Basic player definition
    p2 = Player("Pepino", 15, 10, 5, 19)
    assert_equal(p2.name, "Pepino")
    assert_equal(p2.maxEnergy, 15)
    assert_equal(p2.maxSkill, 10)
    assert_equal(p2.maxMagic, 5)
    assert_equal(p2.maxLuck, 19)
    assert_equal(p2.energy, 15)
    assert_equal(p2.skill, 10)
    assert_equal(p2.magic, 5)
    assert_equal(p2.luck, 19)
    assert_equal(p2.gold, 0)
    assert_equal(p2.backpack, [])
    assert_equal(p2.scroll, [])
    assert_equal(p2.armor, None)
    assert_equal(p2.weapon, None)
    assert_equal(p2.offhand, None)

    # Check if all gets are working
    assert_equal(p2.getName(), "Pepino")
    assert_equal(p2.getMaxEnergy(), 15)
    assert_equal(p2.getMaxSkill(), 10)
    assert_equal(p2.getMaxMagic(), 5)
    assert_equal(p2.getMaxLuck(), 19)
    assert_equal(p2.getEnergy(), 15)
    assert_equal(p2.getSkill(), 10)
    assert_equal(p2.getMagic(), 5)
    assert_equal(p2.getLuck(), 19)
    assert_equal(p2.getGold(), 0)
    assert_equal(p2.getBackpack(), [])
    assert_equal(p2.getScroll(), [])
    assert_equal(p2.getArmor(), None)
    assert_equal(p2.getWeapon(), None)
    assert_equal(p2.getOffhand(), None)

    #Create a player with some items
    p3 = Player("Catatau", 20, 20, 20, 20, ["Vela"], ["energy", "illusion"], "Chestplate", "Short Sword", "Small Shield", 150)
    assert_equal(p3.getName(), "Catatau")
    assert_equal(p3.getMaxEnergy(), 20)
    assert_equal(p3.getMaxSkill(), 20)
    assert_equal(p3.getMaxMagic(), 20)
    assert_equal(p3.getMaxLuck(), 20)
    assert_equal(p3.getEnergy(), 20)
    assert_equal(p3.getSkill(), 20)
    assert_equal(p3.getMagic(), 20)
    assert_equal(p3.getLuck(), 20)
    assert_equal(p3.getGold(), 150)
    assert_equal(p3.getBackpack(), ["Vela"])
    assert_equal(p3.getScroll(), ["energy", "illusion"])
    assert_equal(p3.getArmor(), "Chestplate")
    assert_equal(p3.getWeapon(), "Short Sword")
    assert_equal(p3.getOffhand(), "Small Shield")

def test_sets():
    # Check if every set works proprerly
    p1 = Player("Avestruz")
    p1.setName("Pepino")
    assert_equal(p1.getName(), "Pepino")

    # Check if every set not allow negative numbers
    p1.setMaxEnergy(5)
    assert_equal(p1.getMaxEnergy(), 5)
    p1.setMaxEnergy(-10)
    assert_equal(p1.getMaxEnergy(), 0)

    p1.setMaxSkill(5)
    assert_equal(p1.getMaxSkill(), 5)
    p1.setMaxSkill(-10)
    assert_equal(p1.getMaxSkill(), 0)

    p1.setMaxMagic(5)
    assert_equal(p1.getMaxMagic(), 5)
    p1.setMaxMagic(-10)
    assert_equal(p1.getMaxMagic(), 0)

    p1.setMaxLuck(5)
    assert_equal(p1.getMaxLuck(), 5)
    p1.setMaxLuck(-10)
    assert_equal(p1.getMaxLuck(), 0)

    p1.setMaxEnergy(50)
    p1.setMaxSkill(50)
    p1.setMaxMagic(50)
    p1.setMaxLuck(50)

    p1.setEnergy(5)
    assert_equal(p1.getEnergy(), 5)
    p1.setEnergy(-10)
    assert_equal(p1.getEnergy(), 0)

    p1.setSkill(5)
    assert_equal(p1.getSkill(), 5)
    p1.setSkill(-10)
    assert_equal(p1.getSkill(), 0)

    p1.setMagic(5)
    assert_equal(p1.getMagic(), 5)
    p1.setMagic(-10)
    assert_equal(p1.getMagic(), 0)

    p1.setLuck(5)
    assert_equal(p1.getLuck(), 5)
    p1.setLuck(-10)
    assert_equal(p1.getLuck(), 0)

    p1.setGold(200)
    assert_equal(p1.getGold(), 200)
    p1.setGold(-800)
    assert_equal(p1.getGold(), 0)

    # Check if every set not allow the attribute to exceed the max ammount
    p1.setEnergy(99)
    assert_equal(p1.getEnergy(), p1.getMaxEnergy())

    p1.setSkill(99)
    assert_equal(p1.getSkill(), p1.getMaxSkill())

    p1.setMagic(99)
    assert_equal(p1.getMagic(), p1.getMaxMagic())

    p1.setLuck(99)
    assert_equal(p1.getLuck(), p1.getMaxLuck())

    # Check if change equipment works
    p1.equipArmor("Chestplate")
    assert_equal(p1.getArmor(), "Chestplate")
    p1.equipArmor()
    assert_equal(p1.getArmor(), "Chestplate")

    p1.equipWeapon("Short Sword")
    assert_equal(p1.getWeapon(), "Short Sword")
    p1.equipWeapon()
    assert_equal(p1.getWeapon(), "Short Sword")

    p1.equipOffhand("Small Shield")
    assert_equal(p1.getOffhand(), "Small Shield")
    p1.equipOffhand()
    assert_equal(p1.getOffhand(), "Small Shield")

    # Check if backpack management works
    # Empty backpack (insert)
    p1.putOnBackpack("Candy")
    assert_equal(p1.getBackpack(), ["Candy"])

    # Non-empty backpack (insert)
    p1.putOnBackpack("Wolf")
    assert_equal(p1.getBackpack(), ["Candy", "Wolf"])

    # Non-empty backpack (remove)
    p1.takeFromBackpack("Candy")
    assert_equal(p1.getBackpack(), ["Wolf"])

    # Remove non-existent item from backpack
    p1.takeFromBackpack("Candy")
    assert_equal(p1.getBackpack(), ["Wolf"])

    # Empty backpack (remove)
    p1.takeFromBackpack("Wolf")
    p1.takeFromBackpack("Candy")
    assert_equal(p1.getBackpack(), [])

    # Check if scroll management works
    # Add scroll
    p1.addScroll("levitate")
    assert_equal(p1.getScroll(), ["levitate"])

    # Remove scroll
    p1.useScroll("levitate")
    assert_equal(p1.getScroll(), [])

    # Remove scroll that doesn't exist
    # Remove scroll from empty list
    p1.useScroll("levitate")
    assert_equal(p1.getScroll(), [])

def test_testyourluck():
    p1 = Player("Avestruz", 100, 100, 100, 15)

    result = p1.testYourLuck()
    assert_equal(result, 'good')
    assert_equal(p1.getLuck(), 14)

    p1.setLuck(-12)
    result = p1.testYourLuck()
    assert_equal(result, 'bad')
    assert_equal(p1.getLuck(), 1)

    p1.setLuck(-1)
    result = p1.testYourLuck()
    assert_equal(result, 'bad')
    assert_equal(p1.getLuck(), 0)
