package com.ssafy.model.dto;

import java.util.Arrays;

public class Person {
    private String id;
    private String password;
    private String name;
    private String address;
    private String phone;
    private String eatFood;
    public String getEatFood() {
		return eatFood;
	}

	public void setEatFood(String eatFood) {
		this.eatFood = eatFood;
	}
	private String[] alergy;
    
    
    public Person() {
        super();
        // TODO Auto-generated constructor stub
    }

    public Person(String id, String password, String name, String address, String phone, String[] alergy) {
        this.id = id;
        this.password = password;
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.alergy = alergy;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }
    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public String[] getAlergy() {
        return alergy;
    }
    public void setAllergy(String[] alergy) {
        this.alergy = alergy;
    }
    public String getAllergyAsString() {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<this.alergy.length; i++) {
            sb.append(this.alergy[i]);
            if (i != this.alergy.length - 1)
                sb.append(",");
        }
        return sb.toString();
    }
    @Override
    public String toString() {
        return "Person [name=" + name + ", id=" + id + ", password=" + password + ", allergy=" + Arrays.toString(alergy) + "]";
    }
}