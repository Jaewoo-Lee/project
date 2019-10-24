package com.example.demo.post.dto;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.format.annotation.DateTimeFormat;

import lombok.Data;

@Data
@Entity
@Table(name = "post")
public class Post {
	@Column
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer postNum;
	
	@Column
	private String postTitle;
	
	@Column
	private String postContent;
	
	@UpdateTimestamp
	@DateTimeFormat(pattern = "yyyy-MM-dd'T'HH:mm")
	@Column
	private LocalDateTime postDatetime;
	
	@Column
	private String userId;
}
