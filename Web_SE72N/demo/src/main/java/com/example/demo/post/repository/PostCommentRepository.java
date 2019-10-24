package com.example.demo.post.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.post.dto.PostComment;

public interface PostCommentRepository extends JpaRepository<PostComment, Integer>{

	@Modifying
	@Transactional
	@Query(value = "DELETE FROM PostComment WHERE postNum = ?1")
	void deleteByPostNum(int postNum);
}
