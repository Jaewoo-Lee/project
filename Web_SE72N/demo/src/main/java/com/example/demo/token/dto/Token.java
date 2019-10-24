package com.example.demo.token.dto;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name="token")
public class Token {
	
	@Column
	@Id
	private String tokenInfo;
}
