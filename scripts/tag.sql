  SELECT
      t.id,
      t.name,
      t.main_id,
      t.parent_id,
      t.category_id,
      mt.name as main_tag_name,
      pt.name as parent_tag_name,
      COUNT(tg.id) as usage_count,
      t.followers
  FROM ask_tags t
  INNER JOIN ask_taggables tg ON t.id = tg.tag_id
  LEFT JOIN ask_tags mt ON t.main_id = mt.id
  LEFT JOIN ask_tags pt ON t.parent_id = pt.id
  GROUP BY t.id
  ORDER BY usage_count DESC, t.followers DESC;