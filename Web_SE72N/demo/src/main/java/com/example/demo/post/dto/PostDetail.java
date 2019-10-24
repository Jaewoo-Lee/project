package com.example.demo.post.dto;

import java.time.LocalDateTime;
import java.util.List;

import lombok.Data;

@Data
public class PostDetail {
	private Integer postNum;
	private String postTitle;
	private String postContent;
	private LocalDateTime postDatetime;
	private String userId;
	private List<PostComment> commentList;
	
	public PostDetail(Post p){
		this.postNum = p.getPostNum();
		this.postTitle = p.getPostTitle();
		this.postContent = p.getPostContent();
		this.postDatetime = p.getPostDatetime();
		this.userId = p.getUserId();
	}
}
