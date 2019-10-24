package com.example.demo.user.dto;
//DTO

import lombok.Data;

@Data
public class UserInfo {
	private String userId;
	private String githubId;
	private String authority;
}
