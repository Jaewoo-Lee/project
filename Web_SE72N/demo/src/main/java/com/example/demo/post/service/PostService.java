package com.example.demo.post.service;

import java.util.List;

import com.example.demo.post.dto.Post;
import com.example.demo.post.dto.PostComment;
import com.example.demo.post.dto.PostDetail;

public interface PostService {
	// 포스트 리스트 조회
	public List<PostDetail> searchAllPost();
	
	// 포스트 글 작성 및 수정
	public List<PostDetail> addPost(Post p);
	
	// 포스트 댓글 작성 및 수정
	public List<PostDetail> writePostComment(PostComment postComment);
	
	// 포스트 글 삭제
	public List<PostDetail> deleteOne(int postNum);
	
	// 포스트 댓글 삭제
	public List<PostDetail> deletePostComment(int postcommentNum);
}
