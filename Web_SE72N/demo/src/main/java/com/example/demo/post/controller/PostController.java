package com.example.demo.post.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.post.dto.Post;
import com.example.demo.post.dto.PostComment;
import com.example.demo.post.dto.PostDetail;
import com.example.demo.post.service.PostService;

import lombok.extern.slf4j.Slf4j;

@CrossOrigin
@Controller
@Slf4j
public class PostController {
	@Autowired
	private PostService postService;
	
	// 포스트 리스트 조회
	@GetMapping("/searchAllPost.do")
	public ResponseEntity<List<PostDetail>> searchAllPost() {
		log.debug("post 리스트 호출");
		return new ResponseEntity<List<PostDetail>>(postService.searchAllPost(), HttpStatus.OK);
	}
	
	// 포스트 글 작성 및 수정
	@PostMapping("/newPost.do")
	public ResponseEntity<List<PostDetail>> addPost(@RequestBody Post post){
		log.debug("post 저장 요청");
		return new ResponseEntity<List<PostDetail>>(postService.addPost(post), HttpStatus.OK);
	}
	
	// 포스트 댓글 작성 및 수정
	@PostMapping("/writePostComment.do")
	public ResponseEntity<List<PostDetail>> writeComment(@RequestBody PostComment postComment){
		log.debug("postComment 저장 요청");
		return new ResponseEntity<List<PostDetail>>(postService.writePostComment(postComment), HttpStatus.OK);
	}
	
	// 포스트 글 삭제
	@DeleteMapping("/deletePost.do")
	public ResponseEntity<List<PostDetail>> deletePost(@RequestParam int postNum){
		log.debug(postNum + "번 post 게시글 삭제 요청");
		return new ResponseEntity<List<PostDetail>>(postService.deleteOne(postNum), HttpStatus.OK);
	}
	
	// 포스트 댓글 삭제
	@DeleteMapping("/deletePostComment.do")
	public ResponseEntity<List<PostDetail>> deletePostComment(@RequestParam int postcommentNum){
		log.debug(postcommentNum + "번 postComment 댓글 삭제 요청");
		return new ResponseEntity<List<PostDetail>>(postService.deletePostComment(postcommentNum), HttpStatus.OK);
	}
	
}
