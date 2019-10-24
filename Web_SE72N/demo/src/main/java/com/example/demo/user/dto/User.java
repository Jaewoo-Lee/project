package com.example.demo.user.dto;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name = "user")
public class User {
	@Column
	@Id
	private String userId;
	
	@Column
	private String userPass;
	
	@Column
	private String githubId;
}
