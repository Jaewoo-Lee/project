package com.example.demo.post.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import com.example.demo.portfolio.dto.Portfolio;
import com.example.demo.portfolio.dto.PortfolioComment;
import com.example.demo.portfolio.dto.PortfolioDetail;
import com.example.demo.post.dto.Post;
import com.example.demo.post.dto.PostComment;
import com.example.demo.post.dto.PostDetail;
import com.example.demo.post.repository.PostCommentRepository;
import com.example.demo.post.repository.PostRepository;

@Service
public class PostServiceImpl implements PostService {
	@Autowired
	private PostRepository postRepository;
	@Autowired
	private PostCommentRepository postCommentRepository;

	// 포스트 리스트 조회
	@Override
	public List<PostDetail> searchAllPost() {
		List<Post> plist = postRepository.findAll(new Sort(Sort.Direction.DESC, "postNum"));
		List<PostComment> pclist = postCommentRepository.findAll(new Sort(Sort.Direction.ASC, "postcommentNum"));
		List<PostDetail> pdlist = new ArrayList<>();
		for (Post p : plist) {
			PostDetail temp = new PostDetail(p);
			List<PostComment> tempList = new ArrayList<>();
			for (PostComment pc : pclist) {
				if(temp.getPostNum().equals(pc.getPostNum())) {
					tempList.add(pc);
				}
			}
			temp.setCommentList(tempList);
			pdlist.add(temp);
		}
		return pdlist;
	}

	// 포스트 글 작성 및 수정
	@Override
	public List<PostDetail> addPost(Post post) {
		if(post.getPostNum() == -1) post.setPostNum(null);
		postRepository.save(post);
		return searchAllPost();
	}

	// 포스트 댓글 작성 및 수정
	@Override
	public List<PostDetail> writePostComment(PostComment postComment) {
		if(postComment.getPostcommentNum() == -1) postComment.setPostcommentNum(null);
		postCommentRepository.save(postComment);
		return searchAllPost();
	}

	// 포스트 글 삭제
	@Override
	public List<PostDetail> deleteOne(int postNum) {
		postRepository.deleteById(postNum);
		postCommentRepository.deleteByPostNum(postNum);
		return searchAllPost();
	}

	// 포스트 댓글 삭제
	@Override
	public List<PostDetail> deletePostComment(int postcommentNum) {
		postCommentRepository.deleteById(postcommentNum);
		return searchAllPost();
	}
}
